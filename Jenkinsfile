pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t innovate-analytics/ml-app:${BUILD_NUMBER} .'
                sh 'docker tag innovate-analytics/ml-app:${BUILD_NUMBER} innovate-analytics/ml-app:latest'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker push innovate-analytics/ml-app:${BUILD_NUMBER}'
                    sh 'docker push innovate-analytics/ml-app:latest'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh 'kubectl apply -f kubernetes/service.yaml'
                sh 'kubectl set image deployment/ml-app ml-app=innovate-analytics/ml-app:${BUILD_NUMBER}'
            }
        }
    }
}