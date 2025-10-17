pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                // checkout code
            }
        }
        stage('Build') {
            steps {
                // build commands
            }
        }
        // Add the Serve HTML stage here:
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
