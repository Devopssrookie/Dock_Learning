pipeline {
    agent any
    stages {
        stage('Add directory to PATH') {
            steps {
                script {
                    // Add the directory containing gunicorn to the PATH
                    env.PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
                }
            }
        }
        stage('Check PATH') {
            steps {
                script {
                    // Print the updated value of the PATH environment variable
                    echo "Updated PATH: ${env.PATH}"
                }
            }
        }
        stage('Deploy') {
            steps {
                // Change to the project directory
                dir('/var/lib/jenkins/workspace/Demo_1/Proj_dep') {
                    // Run gunicorn command here
                    sh 'gunicorn frst_proj.wsgi:application --bind 0.0.0.0:8000 --daemon'
                }
            }
        }
    }
}
