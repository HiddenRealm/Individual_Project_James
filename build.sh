sudo apt-get update -y
sudo apt-get install -y python
sudo apt-get install -y python-pip python-dev
sudo apt-get install -y python3-venv
sudo apt-get install -y virtualenv

. ./application/venv/bin/activate
sudo pip install -r requirements.txt

export FLASK_APP=run.py
export FLASK_ENV=production
export FLASK_RUN_HOST 0.0.0.0
export FLASK_RUN_PORT 5000
export FLASK_RUN_CERT cert.pem
export FLASK_RUN_KEY key.pem

flask run
