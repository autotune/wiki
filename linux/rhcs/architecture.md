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

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/sqlstgnd1/sqlstgnd1.vdi" --size 10000 --variant Fixed

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/sqlstgnd2/sqlstgnd2.vdi" --size 10000 --variant Fixed

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/shared/qdisk.vdi" --size 10000 --variant Fixed  

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/shared/data.vdi" --size 10000 --variant Fixed  

    VboxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/shared/docroot_data.vdi" --size 10000 --variant Fixed

2.0 Attach hard disks

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 0 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/sqlstgnd1/sqlstgnd1.vdi --mtype shareable

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 1 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/shared/data.vdi --mtype shareable 

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 2 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/shared/qdisk.vdi --mtype shareable

    VboxManage storageattach sqlstgnd1 --storagectl mysqlstgclu --port 3 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/shared/docroot_data.vdi --mtype shareable

     VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 0 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/sqlstgnd2/sqlstgnd2.vdi --mtype shareable

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 1 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/shared/data.vdi --mtype shareable 

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 2 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/shared/qdisk.vdi --mtype shareable

    VboxManage storageattach sqlstgnd2 --storagectl mysqlstgclu --port 3 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/shared/docroot_data.vdi --mtype shareable


2. PACKAGES

rgmanager

lvm2-cluster

gfs2-utils

ccs
