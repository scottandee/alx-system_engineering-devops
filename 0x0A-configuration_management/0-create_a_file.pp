# This manifest creates a file with name 'school'
# in the /tmp directory


file { '/tmp/school':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
