pipeline {
    agent {
        docker {
            image 'python:3.8' 
            args '-v /root/.cache/pip:/root/.cache/pip'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requisitos.txt'
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    sh 'python -m unittest discover'
                }
            }
        }
    }

    post {
        success {
            echo 'Build e Testes concluídos com sucesso!'
        }
        unstable {
            echo 'Build bem-sucedido, mas alguns testes falharam.'
        }
        failure {
            echo 'Falha no Build.'
        }
    }
}
