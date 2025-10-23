pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
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
                    reportDir: '.',
                    reportFiles: 'Calculator.html',
                    reportName: 'Tax Calculator',
                    reportTitles: 'Calculator Output',
                    keepAll: true,
                    allowMissing: false,
                    alwaysLinkToLastBuild: true
                ])
            }
        }
    }

    post {
        success {
            script {
                // Generate a clickable URL to the HTML artifact
                def buildNumber = currentBuild.number
                def jenkinsUrl = env.JENKINS_URL
                echo "\n✅ Build successful! Open your calculator here:"
                echo "${jenkinsUrl}job/${env.JOB_NAME}/${buildNumber}/artifact/Calculator.html\n"
            }
        }
        failure {
            echo "❌ Build failed. Please check logs for details."
        }
    }
}
