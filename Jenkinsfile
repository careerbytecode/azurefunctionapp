pipeline {
    agent any

    environment {
        TF_PATH = '/usr/bin/terraform' // Adjust if Terraform is installed elsewhere
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/careerbytecode/azurefunctionapp'
            }
        }
        stage('Verify Directory') {
            steps {
                sh 'ls -la'
            }
        }
        stage('Terraform Init') {
            steps {
                dir('devops/infrastructure') {
                    sh 'pwd && ls -la' // Debugging
                    script {
                        sh "${TF_PATH} init"
                    }
                }
            }
        }
        stage('Terraform Validate') {
            steps {
                dir('devops/infrastructure') {
                    sh 'pwd && ls -la' // Debugging
                    script {
                        sh "${TF_PATH} validate"
                    }
                }
            }
        }
        stage('Terraform Plan') {
            steps {
                dir('devops/infrastructure') {
                    sh 'pwd && ls -la' // Debugging
                    script {
                        sh "${TF_PATH} plan -out=tfplan"
                    }
                }
            }
        }
        stage('Terraform Apply') {
            steps {
                dir('devops/infrastructure') {
                    input "Do you want to apply the Terraform plan?" // Optional
                    sh 'pwd && ls -la' // Debugging
                    script {
                        sh "${TF_PATH} apply -auto-approve tfplan"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Terraform deployment completed successfully.'
        }
        failure {
            echo 'Terraform deployment failed.'
        }
    }
}
