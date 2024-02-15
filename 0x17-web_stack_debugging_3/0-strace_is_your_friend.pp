# replacing the false extention aphpp with php 
exec { 'fixing wp settings':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
    path => '/usr/bin',
}
