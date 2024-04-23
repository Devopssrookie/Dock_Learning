pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Checkout the code from Git
                git branch: 'main', url: 'https://github.com/Devopssrookie/Dock_Learning.git'

                // Build the Docker image
                script {
                    docker.build('frst_proj_image', '.')
                }
            }
        }
        stage('Deploy') {
            steps {
                // Run the Docker container
                script {
                    dockerImage = docker.image('frst_proj_image')
                    dockerImage.run('-p 8000:8000 --name frst_proj_container', 'frst_proj_image')
                }
            }
        }
    }
}
