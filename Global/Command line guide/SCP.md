Description :  
Permet de transferer des fichiers via une connexion ssh de façon sécurisée.

Cheat sheet :

```
 cheat.sheets:scp

# scp

# Secure copy (remote file copy program)

# Securely copies files from remote ADDR's PATH to the current-working-directory.

# By default here, port 22 is used, or whichever port is otherwise configured.

scp ADDR:PATH ./

# Using aliases (not Bash aliases) work with scp(1) as well. In this example, -

# the PATH1 of the first remote source defined as ALIAS1 is sent to PATH2 of

# the remote destination defined as ALIAS2.

scp ALIAS1:PATH1 ALIAS2:PATH2

# You can use the `-P` flag -- uppercase, unlike ssh(1) -- to determine the

# PORT, in-case it's non-standard (not 22) or not defined within an alias.

scp -P PORT ADDR:PATH ./

 cheat:scp

# To copy a file from your local machine to a remote server:

scp <file> <user>@<host>:<dest>

# To copy a file from a remote server to your local machine:

scp <user>@<host>:<src> <dest>

# To scp a file over a SOCKS proxy on localhost and port 9999 (see ssh for tunnel setup):

scp -o "ProxyCommand nc -x 127.0.0.1:9999 -X 4 %h %p" <file> <user>@<host>:<dest>

# To scp between two remote servers from the third machine:

scp -3 <user>@<host1>:<src> <user>@<host2>:<dest>

 tldr:scp

# scp

# Secure copy.

# Copy files between hosts using Secure Copy Protocol over SSH.

# More information: <https://man.openbsd.org/scp>.

# Copy a local file to a remote host:

scp path/to/local_file remote_host:path/to/remote_file

# Use a specific port when connecting to the remote host:

scp -P port path/to/local_file remote_host:path/to/remote_file

# Copy a file from a remote host to a local directory:

scp remote_host:path/to/remote_file path/to/local_directory

# Recursively copy the contents of a directory from a remote host to a local directory:

scp -r remote_host:path/to/remote_directory path/to/local_directory

# Copy a file between two remote hosts transferring through the local host:

scp -3 host1:path/to/remote_file host2:path/to/remote_directory

# Use a specific username when connecting to the remote host:

scp path/to/local_file remote_username@remote_host:path/to/remote_directory

# Use a specific ssh private key for authentication with the remote host:

scp -i ~/.ssh/private_key local_file remote_host:/path/remote_file
```