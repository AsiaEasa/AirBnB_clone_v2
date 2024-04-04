exec { 'apt-update-upgrade':
  command => 'apt-get update && apt-get upgrade -y',
  path    => '/usr/bin',
}

package { 'apache2':
  ensure => installed,
}

file { ['/data/web_static', '/data/web_static/releases', '/data/web_static/shared']:
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'root',
  group   => 'root',
  mode    => '644',
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'root',
  group   => 'root',
  require => File['/data/web_static/releases/test/index.html'],
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => [Package['apache2'], File['/data/web_static/current']],
}
