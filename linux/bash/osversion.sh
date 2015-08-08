#!/usr/bin/bash
# distro version
# No LSB modules are available.
# Distributor ID:	Ubuntu
# Description:	Ubuntu 12.04.3 LTS
# Release:	12.04
# Codename:	precise

display_dist(){ 
  lsb_release -a
}

display_dist
