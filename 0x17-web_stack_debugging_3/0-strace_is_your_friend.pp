# This manifest fixes the broken
# wordpress webstack

exec { 'fix-wordpress':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => ['/usr/bin', '/bin']
}
