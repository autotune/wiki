#### Galera Clustering [1]
3 nodes across 3 datacenters:

1 x Load Balancer in IAD
   => add g2 and g3 as external nodes

galera1 => 127.0.1.1 (IAD)
           127.0.1.1
           Pub: 127.0.1.1
           root: GENERATED 
           sst_user: GENERATED
 
galera2 => 127.0.2.1 (ORD)
           127.0.2.1
galera3 => 127.0.3.1 (DFW)
	   127.0.3.1 

Notes: selinux disabled by default in cloud. 
       MAKE SURE you only specify IPs that are reachable by all servers in server.conf. Using 127.0.0.1 as part of the cluster will cause any node to fail to start. 
       MyISAM is not supported. 
       Databases must be designed around Galera Cluster and limitations for full functionality. 

### Install MariaDB Galera Cluster 10.0
Pre-check: yum repolist epel

00) Allow IPs in tables or ports 3306 => mysql, 4567 => replication, 4568 => incremental state transfers, and 4444 => state transfer shots. 

```
iptables -A INPUT -s 127.0.1.1 -j ACCEPT
iptables -A INPUT -s 127.0.2.1 -j ACCEPT
iptables -A INPUT -s 127.0.3.1 -j ACCEPT
iptables-save > /etc/sysconfig/iptables 
```

0) Install mariadb repo

```
printf '[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.0/centos6-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
enabled=1
gpgcheck=1' > /etc/yum.repos.d/mariadb.repo

yum clean all && yum repolist mariadb
```

1) Install socat

```
yum install socat
```

2) Install MariaDB Galera Server, client, and wresp multi-master replciation provider 

```
yum install MariaDB-Galera-server MariaDB-client galera

chkconfig mysql on 

service mysql start 
```

3) Run MySQL secure installation

```
/usr/bin/mysql_secure_installation
```

4) Create MariaDB Cluster users

```
pwgen 500 => change to prefered number

GRANT ALL ON *.* TO 'root'@'localhost' IDENTIFIED BY 'GENERATED'
GRANT ALL ON *.* TO 'sst_user'@'127.0.1.1' IDENTIFIED BY 'GENERATED';
GRANT ALL ON *.* TO 'sst_user'@'127.0.2.1' IDENTIFIED BY 'GENERATED';
GRANT ALL ON *.* TO 'sst_user'@'127.0.3.1' IDENTIFIED BY 'GENERATED';
FLUSH PRIVILEGES;

5) Modify /etc/my.cnf.d/my.cnf

```
[galera]
# Mandatory settings
binlog_format=ROW
default-storage-engine=innodb
innodb_autoinc_lock_mode=2
innodb_locks_unsafe_for_binlog=1
query_cache_size=0
query_cache_type=0
bind-address=0.0.0.0
datadir=/var/lib/mysql
innodb_log_file_size=100M
innodb_file_per_table

wsrep_provider=/usr/lib64/galera/libgalera_smm.so
wsrep_cluster_address="gcomm://127.0.1.1,127.0.2.1,127.0.3.1"
wsrep_cluster_name='galera_cluster'
wsrep_node_address='127.0.3.1'
wsrep_node_name='galera3'
wsrep_sst_method=rsync
wsrep_sst_auth=sst_user:dbpass
binlog_format=row
```


LINKS:

[1] http://galeracluster.com/documentation-webpages/firewallsettings.html
[2] http://tecadmin.net/setup-mariadb-galera-cluster-5-5-in-centos-rhel/
[3] https://mariadb.com/kb/en/mariadb/mariadb-galera-cluster-known-limitations/
