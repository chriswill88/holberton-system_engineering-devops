# This manifest creates a holberton file

file {'/tmp/holberton':
    ensure  => present,
    mode    => '0744',
    group   => 'www-data',
    content => 'I love Puppet',
}
