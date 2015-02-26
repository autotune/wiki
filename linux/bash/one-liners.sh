#!/bin/bash
largest_dirs(){ 
    # specify folders and subfolders to search
    FS='/var';\
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

largest_dirs
