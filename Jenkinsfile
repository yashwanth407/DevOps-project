pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout your repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
                // For demo, listing files (replace with your actual build commands)
                bat 'dir'
            }
        }

        stage('Serve HTML') {
            steps {
                echo 'Starting local server for HTML preview...'
                bat '''
                where python || (
                    echo Python not found, skipping server start.
                    exit 0
                )
                python -m http.server 8080
                '''
            }
        }
    }
}
