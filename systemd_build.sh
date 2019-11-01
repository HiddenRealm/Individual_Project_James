sudo apt-get update
sudo apt install -y python3-pip
sudo apt install -y virtualenv

if [ ! "$(cat /etc/passwd | grep pythonadm)" ];
    then sudo useradd -m -s /bin/bash pythonadm
fi

sudo cp flask-app.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl stop flask-app

install_dir=/opt/flask-app
sudo rm -rf ${install_dir}
sudo mkdir ${install_dir}
sudo cp -r ./* ${install_dir}
sudo chown -R pythonadm:pythonadm ${install_dir}

sudo su - pythonadm << EOF
cd ${install_dir}
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
EOF

sudo systemctl start flask-app

