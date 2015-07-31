#!/bin/bash
largest_dirs(){ 
    # specify folders and subfolders to search
    FS='/';\
    # resize the window and clear, run date
    resize;clear;date;\
    # get total disk size 
    df -h $FS;\
    echo "Largest Directories:";\
    # make find the highest priority process
    # find path, mount, type, print0 to dev/null, pipe to xargs (translate to english)
    nice -n19 find $FS -mount -type d -print0 2>/dev/null|xargs -0\
    du -k |sort -runk1|head -n20|awk '{printf "%8d MB\t%s\n",($1/1024),$NF}';
    echo "Largest Files:"; nice -n 19 find $FS -mount -type f -print0 2>/dev/null| xargs -0 du -k | sort -rnk1| head -n20 |awk '{printf "%8d MB\t%s\n",($1/1024),$NF}';
}

top_ips(){

netstat -antp | awk  '$4 ~ /:443$|:80$/ {c++;print $5 | "sed 's/::ffff://' | sed 's/:.*$//'| sort | uniq -c | sort -nr | head"} END {print c}' 

}

bash_history(){

getent passwd |
cut -d : -f 6 |
sed 's:$:/.bash_history:' |
xargs -d '\n' grep -H -e "$pattern" 

}

delete_error_logs(){

find ./error_log.* -type f -print0 | xargs -0 rm -f

}

add_sudoer(){
sed -i '/run any/a brian  ALL=(ALL)       ALL' /etc/sudoers
}

check_cron(){

for user in $(cut -f1 -d: /etc/passwd);  
do     
    crontab -u $user -l;  
done

}

add_ips() {

# add IPs to an array
# add subinterface number to eth0 based on number of IPs and existing subinterfaces
# then add output to network-scripts

IPS=()
IPS=($(cat ips.txt))
COUNT=34

for IPADDR in "${IPS[@]}" ;
do
    COUNT="$(expr $COUNT + 1)"
    printf "
DEVICE=eth0:$COUNT
IPADDR=$IPADDR
NETMASK=255.255.255.255
ONBOOT=yes\n" > "./ifaces/ifcfg-eth0:$COUNT"

done

}

activate_ips() {

IPS=()
IPS=($(cat ips.txt))
COUNT=34

for IPADDR in "${IPS[@]}" ;
do
    COUNT="$(expr $COUNT + 1)"
    printf "$(/sbin/ifup eth0:$COUNT)\n"
done

}

# refactor
# whois_lookup() {
# DOMAIN=example.com
# whois $(ping -c 1 $DOMAIN|head -n1|awk '{print $3}'|tr '()' ' '|awk '{print $1}'|grep OrgName) 

}# 

sar_mem() {

# show titles of columns 
sar -r|head -n3|tail -n1 && sar -r|tail -n5

}

remove_host() {

ssh-keygen -f "/root/.ssh/known_hosts" -R monit-nagios-a

}

clear_history() {

history -c

}


