pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
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
