# Using pkill to kill a process
exec { 'killmenow':
  path    => '/user/bin',
  command => '/usr/bin/pkill -f killmenow'
  }
