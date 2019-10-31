gcloud compute instances create temp --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud --tags http-server,https-server
gcloud compute firewall-rules create rugby-site --allow tcp:5000 --description "Allow the site to be reached"

gcloud compute ssh -q temp << EOF
   sudo apt update
   sudo apt-get install -y docker 
   sudo apt-get install -y docker.io
   git clone https://github.com/HiddenRealm/Individual_Project_James.git
   cd Individual_Project_James
   sudo docker build -t fantasy-rugby:latest .
   sudo docker run -d -p 5000:5000 fantasy-rugby
EOF
