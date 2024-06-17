pipeline {
    agent any

    stages {
        stage('ChcekOut') {
            steps {
               git url: 'https://github.com/UriDror/pythonProject.git/' , branch: 'main'
            }
        }
        stage('Build') {
            steps {
               sh 'docker build -t uridror/maingame:0.1 .'
            }
        }
        stage('run') {
            steps {
               sh 'docker run -d --name game -p 5000:5000 uridror/maingame:0.1 '
            }
        }
        stage('test') {
            steps {
               sh 'docker exec -d game python e2e.py '
            }
        }
    }
}
