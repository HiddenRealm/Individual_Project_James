sudo apt-get update
sudo apt-get install docker
sudo apt-get install docker.io

sudo usermod -aG docker $USER
newgrp docker
