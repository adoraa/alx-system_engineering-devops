# Add a custom HTTP header with Puppet
# File: 2-puppet_custom_http_response_header.pp

# Update system
exec { 'update system':
    command => '/usr/bin/apt-get update',
}

# Install nginx package
package { 'nginx':
    ensure  => installed,
    require => Exec['update system'],
}

# Define nginx configuration file
file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
}

# Define nginx service
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}

# Define custom HTTP header configuration
file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
}

# Execute command to add custom HTTP header
exec { 'add_custom_http_header':
    command => '/bin/sed -i "24i\        add_header X-Served-By $(facter hostname);" /etc/nginx/sites-available/default',
    require => Package['nginx'],
    notify  => Service['nginx'],
}
