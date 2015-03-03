CHANGE MYSQL DATA DIR

=====================


### SELINUX
```
getenforce
```

### copy over with permissions
```
cp -rp /var/lib/mysql /mnt/data
```

### edit with new values
```
datadir=/mnt/sdb6/mysql/
socket=/mnt/sdb6/mysql.sock
```

### restart mysql
```
/etc/init.d/mysqld restart
```
### without selinux: 

done
