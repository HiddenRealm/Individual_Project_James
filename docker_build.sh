docker build -t fantasy-rugby:latest .
docker run -d -p 5000:5000 --name rugby fantasy-rugby
