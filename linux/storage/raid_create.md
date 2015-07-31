SOFTWARE RAID
=============

RAID 1
======

[root@chef-solo logs]# yum install mdadm -y

[root@chef-solo logs]# mdadm --create --verbose /dev/md0 --level=1 --name=RAID1 --raid-devices=2 /dev/xvdk /dev/xvdl

mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
mdadm: size set to 10477568K
Continue creating array? y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.

[root@chef-solo logs]# fdisk -l|grep md0
Disk /dev/md0: 10.7 GB, 10729029632 bytes
[root@chef-solo logs]# fdisk -l /dev/md0

Disk /dev/md0: 10.7 GB, 10729029632 bytes
2 heads, 4 sectors/track, 2619392 cylinders
Units = cylinders of 8 * 512 = 4096 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

