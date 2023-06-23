# This manifest installs a particular
# version of flask when run

package{'flask':
  ensure   => '2.1.0',
  name     => 'flask'
  command  => '/usr/bin/pip3',
  provider => 'pip3'
}
