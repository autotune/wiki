### VirtualBox 

#### VBoxManage

1) Add a nat network

    VBoxManage modifyvm "rhel7-server" --nic2 natnetwork --nat-network2 "rhel7-network"

#### Networking 

#### Storage

1) Add controller
    VBoxManage storagectl cosnode1 --name cosnode1 --add scsi --bootable on

2) Add hard drive
    VBoxManage createhd --filename "/Volumes/Macintosh HD 2/rhcs/cosnode1/cosnode1" --format VDI --size 10000 --format vdi --variant standard

3) attach hard drive
    VBoxManage storageattach "cosnode1" --storagectl "cosnode1" --port 0 --device 0 --type hdd --medium /Volumes/Macintosh\ HD\ 2/rhcs/cosnode1/cosnode1.vdi

#### Virtual Machines


#### Exercises 

1) Create a standard harddrive 10,000 MB in size

    VBoxManage createhd --filename "/Volumes/Macintosh HD 2/puppet-test" --format VDI --size 10000 --format vdi --variant standard

#### 

https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm

2) Create a virtual machine that uses the "puppet-test" hard drive

Requirements: 
    name: puppet-test
    memory: 1 GB
    architecture: x86_64 CPU
    nic: rhel7-network
    
2a) Create puppet-test vm

    VBoxManage createvm --name puppet-test --basefolder /Volumes/Macintosh HD 2 --register 

2b) Attach controller 
   1) create controller
    VBoxManage storagectl cosnode1 --name cosnode1 --add scsi --bootable on

2c) Attach hard drive
   1) attache hard drive
     
2d) Attach Network Interface Card
