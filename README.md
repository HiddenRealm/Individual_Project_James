# Individual_Project_James
QAC Individual Project

Containerise my project with Docker:   

    Download docker:
      run downlaod_docker.sh
    Restart your terminal
    Run the project in docker:
      run docker_build.sh
    run "docker ps" to check rugby is up & running
    navigate to localhost:5000 to see if the site is up

Containerise my project with Jenkins & Docker:
     
    Enter into file:
      jenkins ALL:ALL NOPASSWD:ALL
      into "sudo visudo"
    Download docker:
      run downlaod_docker.sh
    Restart your terminal

    Log into your jenkins:
      -Go into "Manage Jenkins"
      -Into "Configure Global Security"
      -Turn CSRF off

      go into your jenkins project
      -Enter the repo into the git source section
      -In the execute shell enter
              if sudo docker ps -a | grep "rugby"; then
              sudo docker rm -f rugby
              fi

              sudo docker build -t fantasy-rugby:latest .
              sudo docker run -d -p 5000:5000 --name rugby fantasy-rugby
              sudo docker system prune -af

Run a GCP VM Instance to compile & run my Indiv Project:
    
    Run the project in a gcp instance w/ docker:
      docker_build_GCP.sh
    navigate to {GCP:External-IP}:5000 to see if the site is up
