Boot, reboot, and shut down a system normally:
shutdown --help
	Options:
	  -r                          reboot after shutdown => important. 
	  -h                          halt or power off after shutdown => important.
	  -H                          halt after shutdown (implies -h)
	  -P                          power off after shutdown (implies -h)
	  -c                          cancel a running shutdown
	  -k                          only send warnings, don't shutdown
	  -q, --quiet                 reduce output to errors only
	  -v, --verbose               increase output to include informational messages
	      --help                  display this help and exit
	      --version               output version information and exit
        
EXAMPLE: shutdown -rh now
