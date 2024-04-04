# File: 101-setup_web_static.pp

exec { 'apt-get-update':
	command => 'apt-get update',
		path    => '/usr/bin',
}

exec { 'apt-get-upgrade':
	command => 'apt-get upgrade -y',
		path    => '/usr/bin',
		require => Exec['apt-get-update'],
}

package { 'apache2':
  ensure => installed,
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
  require => File['/data/web_static/releases/test/index.html'],
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => Package['apache2'],
}
