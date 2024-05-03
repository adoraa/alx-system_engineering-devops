## 0x0A. Configuration Management

### Puppet Manifests

This project contains three Puppet manifest files:

- `0-create_a_file.pp`: This manifest creates a file named "school" in the /tmp directory with specific permissions, owner, group, and content.
  
- `1-install_a_package.pp`: This manifest installs the Flask package from pip3, ensuring that it is version 2.1.0.
  
- `2-execute_a_command.pp`: This manifest utilizes the `exec` resource to terminate a process named "killmenow" using the `pkill` command.
