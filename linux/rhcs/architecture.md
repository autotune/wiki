# RHCS Cluster Build

http://bigthinkingapplied.com/creating-a-ha-cluster-with-red-hat-cluster-suite-part-2/

1.0 Cluster Name: mysqlstgclu

2.0 Nodes: sqlstgnd1, sqlstgnd2

3.0 Shared disks

  - 3.1 data.vdi => db files. 

  - 3.2 Shared disk: www_data => web files. 

  - 3.3 Shared disk: qdisk.vdi => quorum disk. 


4.0 Two host-only networks

  - 4.1 

  - 4.2 

### VIRTUAL MACHINE 

VBoxManage createvm --name sqlstgnd1 --basefolder "/Volumes/Macintosh HD 2/rhcs/" --register 

VBoxManage createvm --name sqlstgnd2 --basefolder "/Volumes/Macintosh HD 2/rhcs/" --register 

### STORAGE

#### CONTROLLER 

1.0 Add and attach new controller vm with type as scsi

    VBoxManage storagectl sqlstgnd1 --name mysqlstgclu --add scsi --bootable on

    VBoxManage storagectl sqlstgnd2 --name mysqlstgclu --add scsi --bootable on


#### DISKS

1.0 Create hard disks 

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/shared/qdisk.vdi" --size 10000 --variant Fixed  

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/shared/data.vdi" --size 10000 --variant Fixed  

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/shared/docroot_data.vdi" --size 10000 --variant Fixed

2. PACKAGES

rgmanager

lvm2-cluster

gfs2-utils

ccs
