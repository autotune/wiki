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

#### NODE TEST

[root@controller puppet]# puppet module install packer.tar.gz
    Notice: Preparing to install into /etc/puppet/modules ...
    Notice: Downloading from https://forgeapi.puppetlabs.com ...

    Notice: Installing -- do not interrupt ...
    /etc/puppet/modules
    └─┬ counsyl-packer (v0.9.15)
      └─┬ counsyl-sys (v0.9.18)
	└── puppetlabs-stdlib (v4.6.0)


