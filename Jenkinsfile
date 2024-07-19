pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s src'
            }
        }
    }
}
