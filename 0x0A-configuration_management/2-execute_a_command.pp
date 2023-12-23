# kill the process killmenow

exec {'kill_process':
  path    => '/bin/',
  command => 'pkill killmenow'
}