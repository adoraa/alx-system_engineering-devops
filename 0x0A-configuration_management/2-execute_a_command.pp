# Using pkill to kill a process
exec { 'killmenow':
  path    => '/user/bin',
  command => '/user/bin/pkill -f killmenow',
}
