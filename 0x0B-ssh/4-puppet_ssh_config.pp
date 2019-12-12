# this is a puppet file

file_line { 'id file stuff':
  path => /etc/ssh/ssh_config,
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'psw no':
  path => /etc/ssh/ssh_config,
  line => 'PasswordAuthentication no',
}
