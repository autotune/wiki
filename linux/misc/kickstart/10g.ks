# this installation will install everything needed to get ansible up and running on a server with 10GB of space. 
text
skipx
install
repo --name=updates --mirrorlist=http://mirrorlist.centos.org/?release=6.6&arch=x86_64&repo=updates
repo --name=base --mirrorlist=http://mirrorlist.centos.org/?release=6.6&arch=x86_64&repo=os

repo --name=epel --mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=x86_64

lang en_US.UTF-8
keyboard us
rootpw ch4ng3me
firewall --enable
authconfig --enableshadow --passalgo=sha512
selinux --disabled
timezone Etc/UTC
%include /tmp/kspre.cfg

services --enabled=network,sshd/postfix

network  --bootproto=dhcp --device=eth0 --onboot=on
network  --bootproto=dhcp --device=eth1 --onboot=on

%packages --nobase
at
PyYAML
python-babel
python-crypto
python-crypto2.6
python-httplib2
python-jinja2
python-keyczar
python-paramiko
python-pyasn1
python-simplejson
ansible
acpid
cronie-noanacron
crontabs
logrotate
mailx
mlocate
openssh-clients
openssh-server
postfix
rsync
tmpwatch
vixie-cron
which
wget
yum
vim
-biosdevname
-postfix
-prelink
%end

%pre
bootdrive=sda

if [ -f "/dev/$bootdrive" ] ; then
  exec < /dev/tty3 > /dev/tty3
  chvt 3
  echo "ERROR: Drive device does not exist at /dev/$bootdrive!"
  sleep 5
  halt -f
fi

cat >/tmp/kspre.cfg <<CFG
zerombr
bootloader --location=mbr --driveorder=$bootdrive --append="nomodeset"
clearpart --all --initlabel
part /boot --ondrive=$bootdrive --fstype ext4 --fsoptions="relatime,nodev" --size=512
part pv.1 --ondrive=$bootdrive --size 1 --grow
volgroup vg0 pv.1
logvol / --fstype ext4 --fsoptions="noatime,nodiratime,relatime,nodev" --name=root --vgname=vg0 --size=9000
logvol swap --fstype swap --name=swap --vgname=vg0 --size 1 --grow
CFG

%end

%post
wget -P /root/ 192.168.0.2/post-install.sh
bash post-install.sh
%end
