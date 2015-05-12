### PUPPET
Notes: of course while in prod, we wouldn't run as root. There are also user and group settings to change what daemon runs as, but this is just an initial, very lazy, setup to get up and running. 
Version: 3.7.5
Distro: CentOS release 6.5 (Final)
#### REPO AND INSTALLATION 

rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm

    Packages: puppet-server.noarch

    Installing:
     puppet-server                       noarch                    3.7.5-1.el6                             puppetlabs-products                     24 k
    Installing for dependencies:
     augeas-libs                         x86_64                    1.0.0-7.el6_6.1                         updates                                313 k
     compat-readline5                    x86_64                    5.2-17.1.el6                            C6.0-base                              130 k
     facter                              x86_64                    1:2.4.3-1.el6                           puppetlabs-products                     99 k
     hiera                               noarch                    1.3.4-1.el6                             puppetlabs-products                     23 k
     libselinux-ruby                     x86_64                    2.0.94-5.8.el6                          base                                   100 k
     pciutils                            x86_64                    3.1.10-4.el6                            base                                    85 k
     puppet                              noarch                    3.7.5-1.el6                             puppetlabs-products                    1.6 M
     ruby                                x86_64                    1.8.7.374-4.el6_6                       updates                                538 k
     ruby-augeas                         x86_64                    0.4.1-3.el6                             puppetlabs-deps                         21 k
     ruby-irb                            x86_64                    1.8.7.374-4.el6_6                       updates                                317 k
     ruby-libs                           x86_64                    1.8.7.374-4.el6_6                       updates                                1.7 M
     ruby-rdoc                           x86_64                    1.8.7.374-4.el6_6                       updates                                381 k
     ruby-shadow                         x86_64                    1:2.2.0-2.el6                           puppetlabs-deps                         13 k
     rubygem-json                        x86_64                    1.5.5-3.el6                             puppetlabs-deps                        763 k
     rubygems                            noarch                    1.3.7-5.el6                             base                                   207 k
     virt-what                           x86_64                    1.11-1.2.el6                            base                                    24 k
    Updating for dependencies:
     pciutils-libs                       x86_64                    3.1.10-4.el6                            base                                    34 k

#### /etc/puppet.conf 

dns_alt_names = localhost

#### PUPPET MASTER  

[root@controller ~]# screen -S puppet
[root@controller ~]# puppet master --verbose --no-daemonize
    Info: Creating a new SSL key for ca
    Info: Creating a new SSL certificate request for ca
    Info: Certificate Request fingerprint (SHA256): BA:11:9A:06:54:EE:DF:45:D3:30:4A:C4:D6:85:74:2D:8B:8F:DA:E5:25:81:E1:84:BA:46:F6:F5:6E:AC:25:CC
    Notice: Signed certificate request for ca
    Info: Creating a new certificate revocation list
    Info: Creating a new SSL key for controller
    Info: csr_attributes file loading from /etc/puppet/csr_attributes.yaml
    Info: Creating a new SSL certificate request for controller
    Info: Certificate Request fingerprint (SHA256): 67:BA:C9:CC:62:E7:C6:34:4F:7B:02:52:AF:3B:7F:5A:4A:00:BA:F0:26:6C:B5:76:A2:B4:69:75:39:5A:39:A7
    Notice: controller has a waiting certificate request
    Notice: Signed certificate request for controller
    Notice: Removing file Puppet::SSL::CertificateRequest controller at '/var/lib/puppet/ssl/ca/requests/controller.pem'
    Notice: Removing file Puppet::SSL::CertificateRequest controller at '/var/lib/puppet/ssl/certificate_requests/controller.pem'
Notice: Starting Puppet master version 3.7.5



[root@controller puppet]# puppet resource service puppet ensure=running enable=true
    Notice: /Service[puppet]/ensure: ensure changed 'stopped' to 'running'
    service { 'puppet':
      ensure => 'running',
      enable => 'true',
    }

#### CRON JOB 

puppet resource cron puppet-agent ensure=present user=root minute=30 command='/usr/bin/puppet agent --onetime --no-daemonize --splay'

Notice: /Cron[puppet-agent]/ensure: created
cron { 'puppet-agent':
  ensure  => 'present',
  command => '/usr/bin/puppet agent --onetime --no-daemonize --splay',
  minute  => ['30'],
  target  => 'root',
  user    => 'root',
}
You have new mail in /var/spool/mail/root

#### NODE TEST
