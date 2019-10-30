The following instructions have been tested from a VM running Ubuntu 14.04 and
16.04. Ymmv on other flavors of Linux and versions of Ubuntu.

To set up a dev environment:
1. Install docker:  
    `sudo apt install docker`  
    `sudo groupadd docker`  
    `sudo usermod -aG docker $USER`  
    log out and log back in to have those group changes take effect
1. Install docker-compose:  
    `sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`  
    `sudo chmod +x /usr/local/bin/docker-compose`
1. Install docker-compose command completion (optional):  
    `sudo curl -L https://raw.githubusercontent.com/docker/compose/1.24.1/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose`
1. Download and build docker image, install system & python dependencies:  
    `./exec.py reset`
1. Drop any existing database, create a new database, and run db migrations:  
    `./exec.py reset_db`
1. Create a django superadmin user:  
    `./exec.py manage createsuperuser`
1. Start our server and database containers (append `-d` to run in background):  
    `./exec.py compose up`
1. Open http://localhost:8000/api and/or http://localhost:8000/admin in a browser window within your VM.

