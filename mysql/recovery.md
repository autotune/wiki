### CRASHED TABLES 

    mysqladmin -pr 

    mysqlcheck --repair

    REPAIR TABLES my_neat_table; 

    ```
    +-------------------------+--------+----------+----------+
    | Table                   | Op     | Msg_type | Msg_text |
    +-------------------------+--------+----------+----------+
    | my__neat_table.sessions | repair | status   | OK       | 
    +-------------------------+--------+----------+----------+
    ```

### RESET ROOT PASS

    init-file=/var/lib/mysql/mysql-pass
        => update user set password=PASSWORD("supersecret") where User='root';
    chown mysql:mysql /var/lib/mysql/mysql-pass
    service mysql restart
    /etc/mysql/mysql-init
