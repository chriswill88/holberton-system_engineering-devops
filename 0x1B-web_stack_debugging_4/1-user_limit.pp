# this manifest is for fixing an os error
exec { 'limit':
  command => 'sudo sed -i "s/nofile 4/nofile 6000/g; s/nofile 5/nofile 6000/g" /etc/security/limits.conf',
  path    => ['/bin', '/usr/sbin', '/usr/bin', '/usr'],
}
