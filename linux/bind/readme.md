BIND9 

Distro: CentOS 7

Reference: https://www.digitalocean.com/community/tutorials/how-to-install-the-bind-dns-server-on-centos-6

Notes: starting out with one nameserver for quick setup.

Domain: local.example.com

Config files: /var/named/local.example.zone
              
              /var/named.conf

[root@rhcsa-server ~]# yum install bind bind-utils -y

[root@rhcsa-server ~]# systemctl enable named

[root@rhcsa-server ~]# systemctl start named

ADDED ZONE
==========

/etc/named.conf

zone "local.example.com" IN {
        type master;
        file "local.example.com.zone";
        allow-update { none; };
};


