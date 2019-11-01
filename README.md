# Individual_Project_James
QAC Individual Project

Intro:

    By week 8 of training we had to design, develop and present an individual project, this is mine. 
    The application had to have C.R.U.D functionality. I made a fantasy football knock-off with rugby players. 
    When I was designing my app, I used a Trello board to help break up my tasks and manage my planned sprints, 
    I built the application in a VirtualBox machine with an Ubuntu 16.04 image. 
    I wrote the back end of the application with a mixture of Python3 & Flask, 
    the front end was written in Jinja2, HTML & CSS and the database was an SQLite database.

Pre Requisites:
    
    Clone this repo down
    Check Python3 is installed
    CD into Individual_Project_James

Running the project:
    
    run build.sh
    Navigate to localhost:5000 to see if the site is up
        
Run my project as a SystemD:

    pass

Containerise my project with Docker:   

    Install docker:
      run install_docker.sh
    Restart your terminal

    Run the project in docker:
      run docker_build.sh
    Run "docker ps" to check rugby is up & running
    Navigate to localhost:5000 to see if the site is up

Containerise my project with Jenkins & Docker:

    Enter into file:
      jenkins ALL:ALL NOPASSWD:ALL
      into "sudo visudo"
    Install docker:
      run install_docker.sh
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

    Install GCP to Debian/Ubuntu:
      run install_GCP.sh
    Run the project in a gcp instance w/ docker:
      docker_build_GCP.sh
    navigate to {GCP:External-IP}:5000 to see if the site is up

    If you want to clear the temp VM & firewall:
      run docker_remove_GCP.sh
