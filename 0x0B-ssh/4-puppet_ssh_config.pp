# this is a puppet file



file_line { 'id file stuff':
  path   => /etc/ssh/ssh_config,
  line   => '\tIdentityFile ~/.ssh/holberton',
}

file_line { 'psw no':
  path   => /etc/ssh/ssh_config,
  line   => '\tPasswordAuthentication no',
}
