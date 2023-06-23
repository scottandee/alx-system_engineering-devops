# This manifest installs a particular
# version of flask when run

package{'flask':
  ensure   => '2.1.0',
  command  => '/usr/bin/pip3',
  provider => 'pip3'
}
