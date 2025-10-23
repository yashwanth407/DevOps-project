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
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',               // location of your Calculator.html file
                    reportFiles: 'Calculator.html',
                    reportName: 'Tax Calculator'  // label visible in Jenkins UI
                ])
            }
        }
    }

    post {
        success {
            echo '✅ Build and publish successful! View your calculator in Jenkins.'
        }
        failure {
            echo '❌ Build failed. Please check logs for details.'
        }
    }
}
