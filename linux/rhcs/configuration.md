### NOTES

fencing script => http://meinit.nl/virtualbox-fencing-and-red-hat-enterprise-linux-cluster-suite 

### SERVICES - INSTALLATION

    sudo yum install rgmanager lvm2-cluster gfs2-utils ccs

### SERVICES - CONFIGURATION

#### CMAN

    ssh-keygen => x2


    /etc/init.d/ricci start => x2

    chkconfig ricci on

    ccs_tool addfence sqlstgclu_vbox fence_vbox ipaddr=10.37.129.2 login=bria6265
    
    ccs_tool addnode -n 1 -f sqlstgclu_vbox sqlstgclu1  nodename="vboxNode1"
    
    ccs_tool addnode -n 2 -f sqlstgclu_vbox sqlstgclu2  nodename="vboxNode2"

