pipeline {
    agent any
    environment {
        VENV = ".venv"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mahi3297/python-sample-tests.git'
            }
        }
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

