# RHCS Cluster Build

http://bigthinkingapplied.com/creating-a-ha-cluster-with-red-hat-cluster-suite-part-2/

export MYRHCSDIR="/my/rhcs/dir" 
export DISTRO="/Volumes/Macintosh HD/linuxisos/CentOS-6.5-x86_64-minimal.iso"
export KSURL="https://github.com/autotune/wiki/blob/master/linux/rhcs/ks.cfg"
export ANSCFG="https://github.com/autotune/wiki/blob/master/linux/rhcs/rhcs-playbook.yaml"

1.0 Cluster Name: mysqlstgclu

2.0 Nodes: sqlstgnd1 => 1024MB RAM, sqlstgnd2 => 1024MB RAM

3.0 Shared disks

  - 3.1 data.vdi => db files. 

  - 3.2 Shared disk: www_data => web files. 

  - 3.3 Shared disk: qdisk.vdi => quorum disk. 


4.0 Three host-only networks

  - 4.0 172.0.0.0 => this is used as a placeholder since vboxnet0 would have to map to nic1 if enabled. It will not actually be used. 

  - 4.1 192.168.1.0 => internal network for post-install scripts

  - - 192.168.1.1 => mystgclu1

  --192.168.1.2 => mystgclu2
       
  - 4.2 192.168.2.0 => rhcs network 1
        - 192.168.2.1 => 
        - 192.168.2.2 

  - 4.3 192.168.3.0 => rhcs network 2

### VIRTUAL MACHINE 

1) Create and register virtual machines 

    VBoxManage createvm --name sqlstgnd1 --basefolder "$MYRHCSDIR" --register 
    
    VBoxManage createvm --name sqlstgnd2 --basefolder "$MYRHCSDIR" --register 

2) Modify memory to 1024 MB

    VBoxManage modifyvm sqlstgnd1 --memory 1024
    
    VBoxManage modifyvm sqlstgnd2 --memory 1024

### NETWORKING

1)  Create 3 new host only networks and placeholder. 

    VBoxManage hostonlyif create => x4

    VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.1.0 

    VBoxManage hostonlyif ipconfig vboxnet1 --ip 192.168.2.0

    VBoxManage hostonlyif ipconfig vboxnet2 --ip 192.168.3.0

    VBoxManage hostonlyif ipconfig vboxnet3 --ip 192.168.4.0
    
2)  Attach host only adapters to host networks

    VBoxManage modifyvm sqlstgnd1 --hostonlyadapter2 vboxnet1

    VBoxManage modifyvm sqlstgnd1 --hostonlyadapter3 vboxnet2

    VBoxManage modifyvm sqlstgnd1 --hostonlyadapter4 vboxnet3

    VBoxManage modifyvm sqlstgnd2 --hostonlyadapter2 vboxnet1

    VBoxManage modifyvm sqlstgnd2 --hostonlyadapter3 vboxnet2

    VBoxManage modifyvm sqlstgnd2 --hostonlyadapter4 vboxnet3

3) Add networks to network interfaces on virtual machines
	
    VBoxManage modifyvm sqlstgnd1 --nic1 nat

    VBoxManage modifyvm sqlstgnd1 --nic2 hostonly

    VBoxManage modifyvm sqlstgnd1 --nic3 hostonly

    VBoxManage modifyvm sqlstgnd1 --nic4 hostonly

    VBoxManage modifyvm sqlstgnd2 --nic1 nat

    VBoxManage modifyvm sqlstgnd2 --nic2 hostonly

    VBoxManage modifyvm sqlstgnd2 --nic3 hostonly

    VBoxManage modifyvm sqlstgnd2 --nic4 hostonly


### STORAGE

#### CONTROLLER 

1.0 Add and attach new controller vm with type as scsi

    VBoxManage storagectl sqlstgnd1 --name mysqlstgclu --add scsi --bootable on

    VBoxManage storagectl sqlstgnd2 --name mysqlstgclu --add scsi --bootable on


#### DISKS

1.0 Create hard disks 

    VboxManage createhd --filename "$MYRHCSDIR/sqlstgnd1/sqlstgnd1.vdi" --size 10000 --variant Fixed

    VboxManage createhd --filename "MYRHCSDIR/sqlstgnd2/sqlstgnd2.vdi" --size 10000 --variant Fixed

    VboxManage createhd --filename "$MYRHCSDIR/shared/qdisk.vdi" --size 20 --variant Fixed  

    VboxManage createhd --filename "$MYRHCSDIR/shared/data.vdi" --size 10000 --variant Fixed  

    VboxManage createhd --filename "$MYRHCSDIR/shared/docroot_data.vdi" --size 10000 --variant Fixed

2.0 Attach hard disks

    VBoxManage storageattach "sqlstgnd1" --storagectl "mysqlstgclu" --port 0 --device 0 --type dvddrive --medium "$DISTRO"

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 1 --type hdd --medium "$MYRHCSDIR/sqlstgnd1/sqlstgnd1.vdi" --mtype shareable

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 2 --type hdd --medium "$MYRHCSDIR/shared/data.vdi" --mtype shareable 

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 3 --type hdd --medium "$MYRHCSDIR/shared/qdisk.vdi" --mtype shareable

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 4 --type hdd --medium "$MYRHCSDIR/shared/docroot_data.vdi" --mtype shareable

    VBoxManage storageattach "sqlstgnd2" --storagectl "mysqlstgclu" --port 0 --device 0 --type dvddrive --medium "$DISTRO" 

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 1 --type hdd --medium "$MYRHCSDIR/sqlstgnd2/sqlstgnd2.vdi" --mtype shareable

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 2 --type hdd --medium "$MYRHCSDIR/shared/data.vdi" --mtype shareable 

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 3 --type hdd --medium "$MYRHCSDIR/shared/qdisk.vdi" --mtype shareable

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 4 --type hdd --medium "$MYRHCSDIR/shared/docroot_data.vdi" --mtype shareable

#### INITIAL BOOT 

    VBoxManage startvm sqlstgnd1

    VBoxManage startvm sqlstgnd2


#### TODO


2. PACKAGES

rgmanager

lvm2-cluster

gfs2-utils

ccs
