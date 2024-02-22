# changing the ulimit in the defalut nginx file

exec {'fixing the ulimit in the file':
  command => "sed -i 's/15/unlimited/' /etc/default/nginx",
  path    => ['/bin/', '/usr/bin/']
}

-> exec {'restart nginx':
    command  => 'service nginx restart',
    provider => 'shell'
}
