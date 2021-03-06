# ensure the rabbitmq repo is installed

include packagecloud

 packagecloud::repo { "rabbitmq/rabbitmq-server":
  type => 'rpm',  # or "deb" or "gem"
 }

# install erlang first

exec {"download-erlang-repo":
    command => "curl -O http://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm",
    path => "/bin/:/usr/bin",
    unless => "rpm -q erlang-solutions-1.0-1.noarch"
}

exec{"install-erlang-repo":
    command => "rpm -ivh erlang-solutions-1.0-1.noarch.rpm",
    path => "/bin/:/usr/bin/",
    unless => "rpm -q erlang-solutions-1.0-1.noarch"
}

package {"erlang-solutions":
    ensure => "installed"
}

exec{"clean-yum-cache":
    command => "yum clean all",
    path => "/usr/bin"
}

package { "wget":
    ensure => "installed"
}

package { "erlang":
    ensure => "installed"
}

# install rabbitmq-server and start
package { "rabbitmq-server":
    ensure => "installed"
}

# download config file for guest access
exec{"download-rabbitmq-config":
    command => "curl -o /etc/rabbitmq/rabbitmq.config https://raw.githubusercontent.com/autotune/wiki/master/devops/puppet/rabbitmq/rabbitmq.config",
    unless => "ls -lhd /etc/rabbitmq/rabbitmq.config",
    path => "/bin/:/usr/bin/"
}

service { "rabbitmq-server":
    ensure => "running"
}

# enable control panel
exec{"enable-control-panel":,
    command => "rabbitmq-plugins enable rabbitmq_management",
    path => "/bin/:/usr/bin/:/usr/sbin/:/usr/lib/rabbitmq/bin/"
}
