# this manifest fixes a server

exec { 'sed':
  command => "sed -i 's-phpp-php-g' /var/www/html/wp-settings.php",
  path    => '/bin',
}

