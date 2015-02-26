pvs => list physical volumes

lvs => list logical volumes

fdisk -l /dev/sdb

pvcreate /dev/sdb

vgextend vg_controller /dev/sdb

lvextend -L+10G /dev/mapper/vg_controller-lv_root
