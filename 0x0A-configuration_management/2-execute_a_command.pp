# Using pkill to kill a process
exec { 'killmenow':
  path        => '/usr/bin',
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
}
