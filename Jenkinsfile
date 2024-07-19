pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
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
