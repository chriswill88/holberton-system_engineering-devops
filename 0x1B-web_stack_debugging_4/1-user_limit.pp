# this manifest is for fixing an os error
exec { 'limit':
  command => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 6000/g; s/holberton hard nofile 5/holberton hard nofile 6000/g" /etc/security/limits.conf',
  path    => ['/bin', '/usr/sbin', '/usr/bin', '/usr'],
}
