pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/yashwanth407/DevOps-project'
            }
        }

        stage('Build') {
            steps {
                echo 'Listing files in workspace...'
                bat 'dir'
            }
        }

        stage('Publish Calculator Page') {
            steps {
                echo 'Publishing HTML calculator page to Jenkins UI...'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'Calculator.html',
                    reportName: 'Glass Tax Calculator'
                ])
            }
        }

        stage('Serve HTML (Local Preview)') {
            steps {
                echo 'Starting local server for HTML preview...'
                bat '''
                where python >nul 2>nul
                if %errorlevel% neq 0 (
                    echo Python not found, skipping server start.
                ) else (
                    echo Python found. Starting server on port 8080...
                    start /B python -m http.server 8080
                )
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build completed successfully!'
            echo '📄 You can view the Calculator via: "Glass Tax Calculator" link in Jenkins.'
            echo '🌐 Or, if Python server is running: http://localhost:8080/Calculator.html'
        }
        failure {
            echo '❌ Build failed. Please check logs for details.'
        }
    }
}
