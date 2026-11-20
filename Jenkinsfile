
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t college-event-management:latest .'
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
