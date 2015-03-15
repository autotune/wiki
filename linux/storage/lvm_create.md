[root@web1 ~]# lvs
  /dev/vg2/lvg1: read failed after 0 of 4096 at 799526551552: Input/output error
  /dev/vg2/lvg1: read failed after 0 of 4096 at 799526608896: Input/output error
  /dev/vg2/lvg1: read failed after 0 of 4096 at 0: Input/output error
  /dev/vg2/lvg1: read failed after 0 of 4096 at 4096: Input/output error


[root@web1 mapper]# dmsetup remove vg2-lvg1

Here is the new drive before adding a partition:

[root@web1 mapper]# fdisk -l /dev/sdc

Disk /dev/sdc: 199.4 GB, 199447543808 bytes
255 heads, 63 sectors/track, 24248 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


New partition:

   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1               1       24248   194772028+  83  Linux

Write new filesystem:

[root@web1 mapper]# mkfs -t ext4 /dev/sdc1

[...]

This filesystem will be automatically checked every 28 mounts or
180 days, whichever comes first.  Use tune2fs -c or -i to override.

Create the physical volume: 
[root@web1 mapper]# pvcreate /dev/sdc1
  Physical volume "/dev/sdc1" successfully created

Create the volume group:
[root@web1 mapper]# vgcreate vg2 /dev/sdc1
  Volume group "vg2" successfully created

List volume group details:
[root@web1 mapper]# vgdisplay vg2
  --- Volume group ---
  VG Name               vg2
  System ID
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               185.75 GiB
  PE Size               4.00 MiB
  Total PE              47551
  Alloc PE / Size       0 / 0
  Free  PE / Size       47551 / 185.75 GiB
  VG UUID               gSfwRJ-peZH-uBUb-DQDW-u8OR-tx9x-MpQ8uy


Create the logical volume with 47551 extents (-l %100):

lvcreate --name lvg1 --extents 100%FREE vg2
    Logical volume "lvg1" created

Format new logical volume:

[root@web1 mapper]# mkfs -t ext4 /dev/mapper/vg2-lvg1

Mount new logical volume:

[root@web1 mapper]# mount /dev/mapper/vg2-lvg1 /mnt/data/

Done:

[root@web1 mapper]# df -Th /mnt/data
Filesystem           Type  Size  Used Avail Use% Mounted on
[root@584119-app5 ~]# lvs
  /dev/vg2/lvg1: read failed after 0 of 4096 at 799526551552: Input/output error
  /dev/vg2/lvg1: read failed after 0 of 4096 at 799526608896: Input/output error
  /dev/vg2/lvg1: read failed after 0 of 4096 at 0: Input/output error
  /dev/vg2/lvg1: read failed after 0 of 4096 at 4096: Input/output error


[root@584119-app5 mapper]# dmsetup remove vg2-lvg1

Here is the new drive before adding a partition:

[root@584119-app5 mapper]# fdisk -l /dev/sdc

Disk /dev/sdc: 199.4 GB, 199447543808 bytes
255 heads, 63 sectors/track, 24248 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


New partition:

   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1               1       24248   194772028+  83  Linux

Write new filesystem:

[root@584119-app5 mapper]# mkfs -t ext4 /dev/sdc1

[...]

This filesystem will be automatically checked every 28 mounts or
180 days, whichever comes first.  Use tune2fs -c or -i to override.

Create the physical volume: 
[root@584119-app5 mapper]# pvcreate /dev/sdc1
  Physical volume "/dev/sdc1" successfully created

Create the volume group:
[root@584119-app5 mapper]# vgcreate vg2 /dev/sdc1
  Volume group "vg2" successfully created

List volume group details:
[root@584119-app5 mapper]# vgdisplay vg2
  --- Volume group ---
  VG Name               vg2
  System ID
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               185.75 GiB
  PE Size               4.00 MiB
  Total PE              47551
  Alloc PE / Size       0 / 0
  Free  PE / Size       47551 / 185.75 GiB
  VG UUID               gSfwRJ-peZH-uBUb-DQDW-u8OR-tx9x-MpQ8uy


Create the logical volume with 47551 extents (-l %100):

lvcreate --name lvg1 --extents 100%FREE vg2
    Logical volume "lvg1" created

Format new logical volume:

[root@584119-app5 mapper]# mkfs -t ext4 /dev/mapper/vg2-lvg1

Mount new logical volume:

[root@584119-app5 mapper]# mount /dev/mapper/vg2-lvg1 /mnt/data/

Done:

[root@584119-app5 mapper]# df -Th /mnt/data
Filesystem           Type  Size  Used Avail Use% Mounted on
/dev/mapper/vg2-lvg1
                     ext4  183G   60M  174G   1% /mnt/data/dev/mapper/vg2-lvg1
                     ext4  183G   60M  174G   1% /mnt/data
