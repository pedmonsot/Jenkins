pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               
                git url: 'https://github.com/pedmonsot/Jenkins.git'
            }
        }

        stage('Run Tests') {
            steps {
                
                sh 'python3 -m unittest test_detection.py'
            }
        }
    }
}

