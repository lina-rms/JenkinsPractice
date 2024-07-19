pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requisitos.txt'
            }
        }

        stage('Build and Test') {
            steps {
                sh 'python3 -m unittest discover'
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
