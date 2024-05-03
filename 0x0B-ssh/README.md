# 0x0B-ssh

## Learning Objectives
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

## Files

- **0-use_a_private_key:** Bash script that uses SSH to connect to a server using a specified private key and user.

- **1-create_ssh_key_pair:** Bash script that creates an RSA key pair with specific requirements.

- **100-puppet_ssh_config.pp:** Puppet manifest file to configure the SSH client to use a private key and refuse password authentication.

- **2-ssh_config:** SSH client configuration file.
