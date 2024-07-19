pipeline {
    agent any

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
