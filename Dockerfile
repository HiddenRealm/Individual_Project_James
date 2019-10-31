FROM python:2.7

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_APP run.py
ENV FLASK_ENV production
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_CERT cert.pem
ENV FLASK_RUN_KEY key.pem
    
COPY . .
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
