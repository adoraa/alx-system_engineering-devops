# File: 2-puppet_custom_http_response_header.pp

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Define nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define custom HTTP header configuration file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "add_header X-Served-By $hostname;",
  notify  => Service['nginx'],
}
