pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1'
        DOCKER_IMAGE = 'frst_proj_image'
        DOCKER_CONTAINER = 'frst_proj_container'
        DOCKER_RUN_OPTIONS = "-p 8000:8000 --name ${DOCKER_CONTAINER}"
    }

    stages {
        stage('Build') {
            steps {
                // Checkout the code from Git
                git 'https://github.com/Devopssrookie/Dock_Learning.git'

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
