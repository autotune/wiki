### VirtualBox 

#### VBoxManage

1) Add a nat network

    VBoxManage modifyvm "rhel7-server" --nic2 natnetwork --nat-network2 "rhel7-network"

#### Networking 

#### Storage

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

2b) Attach hard drive

2c) Attach Network Interface Card
