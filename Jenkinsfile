pipeline{
	agent any
    stages{
		stage('---Build_Image---'){
			steps{
                sh "sudo docker build -t fantasy-rugby:latest ."
            }
        }
		stage('---Clean_Container---'){
			steps{
				sh label: '', script:
				'''
				if [ "$(sudo docker ps -qa -f name=rugby)" ]; then
						sudo docker rm -f rugby
				fi
				'''
			}
		}
		stage('---Build_Container---'){
			steps{
				sh "sudo docker run -d --name rugby -p 5000:5000 fantasy-rugby:latest"
			}
		}
	}
}
