pipeline {
    agent {
        docker {
            dockerfile true
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s src'
            }
        }
    }
}
