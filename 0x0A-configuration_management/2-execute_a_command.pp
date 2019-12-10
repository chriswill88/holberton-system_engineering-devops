# this manifest kills a program

exec {'pkill killmenow':
  path => ['/usr/bin/'],
}
