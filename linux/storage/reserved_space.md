#### RESERVED DISK SPACE

Most filesystems comes with a certain percentage of "reserved disk space," typically about 5%. This can be changed with the following command to only have 1%:

    tune2fs -m 1 /dev/sda1

