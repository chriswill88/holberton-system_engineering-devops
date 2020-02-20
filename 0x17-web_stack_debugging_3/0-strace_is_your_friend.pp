# this manifest fixes a server

file_line { '/var/www/html/wp-settings.php':
  ensure  => present,
  path    => '/var/www/html/wp-settings.php',
  replace => true,
  line    => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match   => 'phpp',
}
