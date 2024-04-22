pipeline {
    agent any
 
    environment {
        DOCKER_IMAGE = 'frst_proj_image'
        DOCKER_CONTAINER = 'frst_proj_container'
        DOCKER_RUN_OPTIONS = "-p 8000:8000 --name ${DOCKER_CONTAINER} --rm"
    }
 
    stages {
        stage('Build') {
            steps {
                // Checkout the code from Git
                checkout scm
 
                // Build the Docker image
                script {
                    docker.build(DOCKER_IMAGE, '.')
                }
            }
        }
        stage('Deploy') {
            steps {
                // Run the Docker container
                script {
                    dockerImage = docker.image(DOCKER_IMAGE)
                    dockerImage.run(DOCKER_RUN_OPTIONS, DOCKER_IMAGE)
                }
            }
        }
    }
}
