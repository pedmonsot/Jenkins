pipeline {
    agent any



        stage('Run Tests') {
            steps {
                
                sh 'python3 -m unittest test_detection.py'
            }
        }
    }
}

