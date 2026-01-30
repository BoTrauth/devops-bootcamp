pipeline {
    agent any /* Use any available executor agent */

    environment {
        /*
           DEFINE YOUR VARIABLES HERE.
           Replace this URL with the output from your Terraform run.
        */
        REGISTRY = '123456789012.dkr.ecr.us-east-1.amazonaws.com/my-flask-app'
        REGION = 'us-east-1'
        IMAGE_TAG = "${BUILD_NUMBER}" 
    }

    stages {
        stage('Checkout') {
            steps {
                /* Pulls code from the branch that triggered the build */
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    /* 
                       Build the image locally.
                       We tag it with the Build Number so every build is unique.
                    */
                    sh "docker build -t $REGISTRY:$IMAGE_TAG ."
                }
            }
        }

        stage('Push to ECR') {
            steps {
                script {
                    /*
                       This is the tricky part. 
                       We need to log in to ECR *inside* the pipeline.
                       This command gets a password from AWS and passes it to docker login.
                    */
                    sh "aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $REGISTRY"
                    
                    /* Push the specific tag */
                    sh "docker push $REGISTRY:$IMAGE_TAG"
                    
                    /* Also push 'latest' so it's easy to find */
                    sh "docker tag $REGISTRY:$IMAGE_TAG $REGISTRY:latest"
                    sh "docker push $REGISTRY:latest"
                }
            }
        }
    }
    
    post {
        always {
            /* Clean up disk space by removing the local image after push */
            sh "docker rmi $REGISTRY:$IMAGE_TAG"
            sh "docker rmi $REGISTRY:latest"
        }
    }
}
