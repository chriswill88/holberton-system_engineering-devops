# adds a custom header

file_line { '/etc/nginx/sites-enabled/default':
  ensure   => 'present',
  match    => '^server {',
  path     => '/etc/nginx/sites-enabled/default',
  line     => "server {\n\tadd_header X-Served-By ${hostname};",
  multiple => true
}

exec { 'service nginx reload':
  path     => ['/usr/bin', '/usr/sbin',],
  provider => shell,
}

