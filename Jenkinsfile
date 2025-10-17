pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
                bat 'dir'
            }
        }

        stage('Serve HTML') {
            steps {
                echo 'Starting local server for HTML preview...'
                bat 'python -m http.server 8080'
            }
        }
    }
}
