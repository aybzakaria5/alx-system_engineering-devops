# Killing killmenow using Puppet
exec { 'killmenow':
  command   => '/usr/bin/pkill',
  arguments => ['-TERM', 'killmenow'],
}
