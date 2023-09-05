# This manifest edits the sshconfig
# file to avoid logins with password

file_line { 'Turn off passwd auth':
  ensure => line,
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure => line
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}
