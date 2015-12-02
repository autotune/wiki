### MYSQL REPLICATION 

### MASTER/SLAVE 

##### MASTER
```
[mysqld]
log-bin=mysql-bin
server-id=1
```

#### TROUBLESHOOTING

"Table doesn't exist": https://www.howtoforge.com/how-to-repair-mysql-replication

mysql> STOP SLAVE;

(set this to however many queries need to be skipped or keep repeating)
mysql> SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;  

mysql> START SLAVE;

mysql -e 'show slave status\G;|grep Last_Error
