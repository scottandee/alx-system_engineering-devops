# This manifest kills a particular 
# process only if it is running

exec{'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/sbin'],
  onlyif  => 'pgrep -f killmenow'
}
