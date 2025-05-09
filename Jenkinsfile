pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/pedmonsot/Jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt || true'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizada.'
        }
        success {
            echo '✅ Las pruebas pasaron correctamente.'
        }
        failure {
            echo '❌ Algunas pruebas fallaron.'
        }
    }
}


