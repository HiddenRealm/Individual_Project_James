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
				sh "sudo docker run -d -p 5000:5000 --name rugby fantasy-rugby:latest"
			}
		}
		stage('---Script_Check---'){
			steps{
				sh label: 'Test', script:
					'''
					echo "Hi"
					echo "2"
					echo "6"
					'''
			}
		}
	}
}
