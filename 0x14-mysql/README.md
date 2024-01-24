# Project: 0x14 MySQL

## Description
This project focuses on MySQL installation, database administration, and setting up a primary-replica infrastructure. The tasks include installing MySQL, creating users, setting up replication, and creating a backup strategy.

## Concepts
- Database administration
- Web stack debugging
- [How to] Install MySQL 5.7

## Resources
- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)
- `mysqldump` command documentation

## Learning Objectives
At the end of this project, you should be able to explain:
- The main role of a database
- What a database replica is and its purpose
- Why database backups need to be stored in different physical locations
- The operation to regularly perform to ensure the database backup strategy works

## Requirements
- Allowed editors: vi, vim, emacs
- Interpreted on Ubuntu 16.04 LTS
- Bash scripts must be executable
- Shellcheck (version 0.3.7-5~ubuntu16.04.1) must pass without any errors
- First line of Bash scripts: `#!/usr/bin/env bash`
- Second line of Bash scripts: Comment explaining the script's purpose
- README.md file at the root of the project folder is mandatory

## Servers Information
| Name           | Username | IP              | State   |
|----------------|----------|------------------|---------|
| 375416-web-01  | ubuntu   | 54.237.12.57    | running |
| 375416-web-02  | ubuntu   | 54.84.10.93     | running |
| 375416-lb-01   | ubuntu   | 54.162.96.5     | running |

## Tasks

### 0. Install MySQL
- Install MySQL 5.7.x on web-01 and web-02 servers.
- Ensure task #3 of the SSH project is completed for both servers.
- Example:
  ```bash
  ubuntu@229-web-01:~$ mysql --version
  mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using EditLine wrapper
  ubuntu@229-web-01:~$
  ```

### 1. Let us in!
- Create a MySQL user named holberton_user on both web-01 and web-02.
- Grant necessary permissions for checking the primary/replica status.
- Ensure task #3 of the SSH project is completed for both servers.
- Example:
  ```bash
  ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
  Enter password:
  +-----------------------------------------------------------------+
  | Grants for holberton_user@localhost                             |
  +-----------------------------------------------------------------+
  | GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
  +-----------------------------------------------------------------+
  ubuntu@229-web-01:~$
  ```

### 2. If only you could see what I've seen with your eyes
- Create a database named tyrell_corp on web-01.
- Create a table named nexus6 within the tyrell_corp database and add at least one entry.
- Grant SELECT permissions to holberton_user.
- Example:
  ```bash
  ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
  Enter password:
  +----+-------+
  | id | name  |
  +----+-------+
  |  1 | Leon  |
  +----+-------+
  ubuntu@229-web-01:~$
  ```

### 3. Quite an experience to live in fear, isn't it?
- Create a new user replica_user on web-01 for the replica server.
- Grant necessary permissions for replication.
- Verify using holberton_user's SELECT privileges on mysql.user table.
- Example:
  ```bash
  ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
  +------------------+-----------------+
  | user             | Repl_slave_priv |
  +------------------+-----------------+
  | root             | Y               |
  | mysql.session    | N               |
  | mysql.sys        | N               |
  | debian-sys-maint | Y               |
  | holberton_user   | N               |
  | replica_user     | Y               |
  +------------------+-----------------+
  ubuntu@229-web-01:~$
  ```

### 4. Setup a Primary-Replica infrastructure using MySQL
- Set up a primary-replica infrastructure with MySQL.
- Primary hosted on web-01, replica on web-02, using tyrell_corp database.
- Provide MySQL primary and replica configurations as answer files.

### 5. MySQL backup
- Write a Bash script to generate a MySQL dump and create a compressed archive.
- MySQL dump must contain all databases, named backup.sql.
- Compress dump to a tar.gz archive with a specific name format.
- Bash script accepts one argument (password for MySQL root user).
- Example:
  ```bash
  ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
  backup.sql
  ubuntu@03-web-01:~$ ls
  01-03-2017.tar.gz  5-mysql_backup  backup.sql
  ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
  01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
  ubuntu@03-web-01:~$
  ```