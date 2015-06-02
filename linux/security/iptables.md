1) Allow all traffic in from one IP

    iptables -A INPUT -s 172.16.0.1 -j ACCEPT 

2) Allow all tcp traffic in through one port

    iptables -A INPUT -m tcp -p tcp --dport 22 -j ACCEPT

3) Allow all tcp traffic in through multiple ports

    iptables -A INPUT -i eth0 -p tcp -m state --state NEW -m multiport --dports 21,80,443 -j ACCEPT
