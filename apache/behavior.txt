Apache Behavior

Service Commands: behavior that specify how apache will act rather than react.  
Start
Restart 
stop
graceful 

Common usage: start/restart/stop/graceful 

Config Preload:  what gets loaded before apache actually does anything
Define
LoadModule 
Include
Common modules: auth_basic_module, rewrite_module, log_config_module, version_module

Architecture: how the layout of apache is configured. 

User/Group: specifies which user and group apache runs as. 
Modules: <IfModule></IfModule>
DocumentRoot: DocumentRoot "/var/www/html"
Per-directory configuration: <Directory "/var/www/html"></Directory>
options (relevant): FollowSymLinks, Indexes
AllowOverride: enable .htaccess. 

Common Modules:
mod_rewrite: 
RewriteBase
RewriteRule
RewriteCondition

Logging: 
ErrorLog: logs/error_log relative to ServerRoot directive

LogLevel
=======
ErrorLog => [date][type][host][error message][file]
AccessLog => %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\ =>  %h[host]%l[correlate in access log]%u[userid in HTTP auth]%t[time]%r[client request in quotes]%User-Agent[exact user agent]
