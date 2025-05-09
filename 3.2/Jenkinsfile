pipeline {
    agent any
    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/pedmonsot/Jenkins.git'
                sh 'rm -rf Jenkins && git clone https://github.com/pedmonsot/Jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt || true'
                dir('Jenkins') {
                    sh 'pip3 install --break-system-packages -r requirements.txt || true'
                }
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                dir('Jenkins') {
                    sh 'python3 -m unittest discover'
                }
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

