pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository (main branch)...'
                git branch: 'main', url: 'https://github.com/yashwanth407/DevOps-project'
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
                publishHTML([
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
                echo 'Attempting to start local server for HTML preview...'
                bat '''
                where python >nul 2>nul
                if %ERRORLEVEL% NEQ 0 (
                    echo Python not found, skipping server start.
                    exit /b 0
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
            echo '✅ Build completed successfully! Calculator page published.'
        }
        failure {
            echo '❌ Build failed. Please check logs for details.'
        }
    }
}
