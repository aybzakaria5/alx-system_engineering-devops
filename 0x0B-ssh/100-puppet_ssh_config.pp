 # puppet file for last task

file_line { 'no PasswordAuthentication needed':
    path  => '/etc/ssh/sshd_config',
    line  => 'PasswordAuthentication no',
    match => '^#?PasswordAuthentication',
}

file_line { 'using the  identity file':
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/.ssh/school',
    match => '^#?IdentityFile',
}
