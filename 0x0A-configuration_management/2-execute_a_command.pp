# kill the process killmenow

exec {'killmenow':
  path    => '/bin/',
  command => 'pkill killmenow'
}