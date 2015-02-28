### CRASHED TABLES 
```
mysqladmin -pr 
mysqlcheck --repair
REPAIR TABLES my_neat_table; 
+-------------------------+--------+----------+----------+
| Table                   | Op     | Msg_type | Msg_text |
+-------------------------+--------+----------+----------+
| my__neat_table.sessions | repair | status   | OK       | 
+-------------------------+--------+----------+----------+
````
