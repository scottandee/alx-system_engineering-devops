# This manifest increases the user limit
# for an nginx web server

exec { 'fix--for-nginx':
  command => 'sed -i "/^ULIMIT/c ULIMIT=\"-n 500\"" /etc/default/nginx; service nginx restart',
  path    => ['/usr/bin', '/bin']
}
