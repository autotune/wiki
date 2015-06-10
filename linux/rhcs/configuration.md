### NOTES

fencing script => http://meinit.nl/virtualbox-fencing-and-red-hat-enterprise-linux-cluster-suite 

### SERVICES - INSTALLATION

    sudo yum install rgmanager lvm2-cluster gfs2-utils ccs

### SERVICES - CONFIGURATION

#### CMAN

    ssh-keygen => x2


    /etc/init.d/ricci start => x2

    chkconfig ricci on

    ccs_tool addfence sqlstgclu_vbox fence_vbox ipaddr=10.37.129.2 login=bria6265
    
    ccs_tool addnode -n 1 -f sqlstgclu_vbox sqlstgclu1  nodename="vboxNode1"
    
    ccs_tool addnode -n 2 -f sqlstgclu_vbox sqlstgclu2  nodename="vboxNode2"

### DISKS

[root@sqlstgclu1 /]# ccs -h localhost --setquorumd label=clusterdisk


#### PHSYICAL PARTITIONS

[root@sqlstgclu1 /]# fdisk -l|grep Linux

/dev/sda1   *           1          66      524288   83  Linux => boot

/dev/sda2              66        1275     9714688   8e  Linux LVM => system disk

/dev/sdb               1          10       80293+  83  Linux => data (lvm cluster)

/dev/sdc               1          20       20464   83  Linux => quorum disk (no lvm)

/dev/sdd               1        1274    10233373+  83  Linux => docroot (lvm cluster)

#### LVM CONFIGURATION

[root@sqlstgclu1 /]# grep "locking_type = " /etc/lvm/lvm.conf|head -n2 => x2
    # locking_type = 1
    locking_type = 3

service clvmd restart => x2

#### LVM PARTITIONS

1.0) Create physical volumes 

 pvcreate /dev/sdd

 pvcreate /dev/sdb

2.0) Create clustered physical volume group

vgcreate -cy vg_sqlstgclu-cluster_data /dev/sdb

vgcreate -cy vg_sqlstgclu-cluster_docroot /dev/sdd

2.1) How to revert if necessary

vgchange -cy vg_sqlstgclu-cluster_data --config 'global {locking_type = 0}'

vgchange -cn vg_sqlstgclu-cluster_docroot --config 'global {locking_type = 0}'


2.2) Create clustered logical volumes 

lvcreate -n lv_data -l 100%vg vg_sqlstgclu-cluster_data

lvcreate -n lv_docroot -l 100%vg vg_sqlstgclu-cluster_docroot

3.0) Activate logical volume group

lvchange -an vg_sqlstgclu-cluster_docroot

lvchange -an vg_sqlstgclu-cluster_data

4.0) Create quorum disk

mkqdisk -c /dev/sdc1 -l clusterdisk

5.0) Create GFS filesystem 

5.1) Create 2 64 bit journals on GFS 

mkfs.gfs2 -t mystgclu:datagfs2 -j 2 -J 64 /dev/vg_sqlstgclu-cluster_data/lv_data

6.0) Start cluster services

1) Start cluster manager

service cman start 

2) start cluster logical volume manager

service clvmd start => x2 

chkconfig clvmd on 

3) start cluster manager (logical volumes will fail to mount unless started)

service rgmanager start 

4) start ricci

service ricci start => x2

ccs -h sqlstgclu2 --sync --activate

7.0) Configure storage resource 

7.1) List storage resource available

    mkqdisk -L|grep -i label
    Label:                clusterdisk

7.2) Create web failover domain

    ccs -h localhost --addfailoverdomain name=web

7.3) Create web resources service group

    ccs -h localhost --addservice web-resources domain=web recovery=relocate

7.4) Add VIP IP to new web-resources subservice

    ccs -h localhost --addsubservice web-resources ip ref=192.168.3.1

7.5) Add filesystems as dependencies for VIP

    ccs -h localhost --addsubservice web-resources ip:clusterfs ref=docrootgfs2
    
    ccs -h localhost --addsubservice web-resources ip:clusterfs[0]:clusterfs ref=datagfs2
 
8.0) Install apache and mysql

    yum install mysql-server -y && yum install httpd -y

    chkconfig mysqld on && chkconfig httpd on


