# this is a puppet file

file_line {
  ensure => present,
  path   => /etc/ssh/ssh_config,
  line   => '\tIdentityFile ~/.ssh/holberton',
}

file_line {
  ensure => present,
  path   => /etc/ssh/ssh_config,
  line   => '\tPasswordAuthentication no',
  match  => 'PasswordAuthentication',
}
