FROM python:2.7

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip

WORKDIR /app
ENV FLASK_ENV production
ENV FLASK_APP run.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
