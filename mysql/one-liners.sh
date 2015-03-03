#!/bin/bash

# remote_privs() {
#   mysql -e "select * from information_schema.user_privileges where grantee like '%';"
# }

slow_query_log() {
  mysql -e "show variables like '%log';"
  # mysql -e 'SET GLOBAL slow_query_log = 'ON';'
  mysql -e "show variables like '%slow%';"
}

slow_query_log
  

