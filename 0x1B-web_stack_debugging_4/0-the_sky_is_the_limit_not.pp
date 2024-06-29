# fix nginx to accept and serve more requests

#increase the ULIMIT of the default file
exec {'modify max open files limit setting':
  command => '/bin/sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin:/bin/',
}
