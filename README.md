## Create Dockerfile

### Description: Automate Dockerfile creation

### Arguments:
#### --fr --> FROM
#### --workdir --> WORKDIR (default path is /usr/src/app)
#### --run --> RUN (required)
#### --cmd --> CMD (required)
#### --filepath (default path is current directory)

### Example:
  ```bash
    create_dockerfile.py --fr "ubuntu:22.04" --run "chmod +x script.sh" --copy "script.sh" --cmd "./script.sh"
  ```
