#### IDEAL CONFIG WITH PIGZ

    /var/log/httpd/*log {
	# compress using pigz maximum of 5 threads
	compress
	compresscmd /usr/bin/pigz
	compressoptions -p5
	size 1G
	missingok
	notifempty
	sharedscripts
	delaycompress
	postrotate
	    /sbin/service httpd reload > /dev/null 2>/dev/null || true
	endscript
    }
