
pipeline {
    agent any

    stages {

        stage('Check Docker') {
            steps {
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" version'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('D:\\college-event-management') {
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t college-event-management:latest .'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                bat(returnStatus: true, script: '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" rm -f college-events')

                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" run -d --restart unless-stopped -p 5000:5000 --name college-events college-event-management:latest'
            }
        }
    }
}
