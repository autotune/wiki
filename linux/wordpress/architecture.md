### WORDPRESS ARCHITECTURE (relevant) 
#### FOLDERS AND FILES

    index.php
    license.txt
    readme.html
    wp-activate.php
    wp-admin 
    wp-blog-header.php
    wp-comments-post.php
    wp-config.php => database info and main config
    wp-config-sample.php
    wp-content
      -> wp-themes
      -> wp-plugins
    wp-cron.php
    wp-includes
    wp-links-opml.php
    wp-load.php
    wp-login.php
    wp-mail.php
    wp-settings.php
    wp-signup.php
    wp-trackback.php
    xmlrpc.php => xmlrpc vulnerability in 3.9.2 or less [1]


#### PERMISSIONS 

 # use ftp user rather than web user

sudo chown root:ftpuser wordpress

sudo chmod 775 wordpress


#### VARIABLES (RELAVENT):
 # debug mode

define('WP_DEBUG', false);

 # connection info

    define('DB_NAME', 'wordpress');
    define('DB_USER', 'wpsite');
    define('DB_PASSWORD', '134qqsdft43FSf');
    # may be using external database
    define('DB_HOST', 'localhost');
 # do not require ftp

    define('FS_METHOD', 'direct');

#### DATABASE 

[1] https://wordpress.org/support/topic/warning-xmlrpc-wordpress-exploit-ddos
[2] http://codex.wordpress.org/Changing_File_Permissions
