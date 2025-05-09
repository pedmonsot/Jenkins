pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
<<<<<<< HEAD
                git 'https://github.com/pedmonsot/Jenkins.git'
=======
                sh 'rm -rf Jenkins && git clone https://github.com/pedmonsot/Jenkins.git'
>>>>>>> 04cb97c (images added)
            }
        }

        stage('Instalar dependencias') {
            steps {
<<<<<<< HEAD
                sh 'pip3 install -r requirements.txt || true'
=======
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
>>>>>>> 04cb97c (images added)
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

<<<<<<< HEAD

=======
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
>>>>>>> 04cb97c (images added)
