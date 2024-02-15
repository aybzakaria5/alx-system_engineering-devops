# replace .phpp with .php in wp-settings.php
exec { 'fixing wp-settings.php':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
