#!/bin/bash
# change me to correct IPs 
webnginxa="10.0.0.1"
webnginxb="10.0.0.2"
lbhaproxya="10.0.0.3"
monitnagiosa="10.0.0.4"
nagios3url="https://raw.githubusercontent.com/autotune/wiki/master/devops/buildout01/nagios3"
nrpeurl=$nagios3url/nagios/nrpe.cfg
nginxurl="https://raw.githubusercontent.com/autotune/wiki/master/devops/buildout01/nginx.conf"
haproxycfg="https://raw.githubusercontent.com/autotune/wiki/master/devops/buildout01/haproxy.cfg"
sudoer="auser"
publickey=''
