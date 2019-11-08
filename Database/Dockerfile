FROM mysql

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip python-dev

COPY . .
RUN pip install -r requirements.txt


CMD python create.sql
COPY ./data.sql /docker-entrypoint-initdb.d/
# CMD mysql -u root --password="password" site < data.sql
