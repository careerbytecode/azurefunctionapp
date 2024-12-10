pipeline {
    agent any

    environment {
        TF_PATH = '/usr/bin/terraform' // Adjust if Terraform is installed elsewhere
        TF_VAR_subscription_id = credentials('AZURE_SUBSCRIPTION_ID')
        TF_VAR_tenant_id       = credentials('AZURE_TENANT_ID')
        TF_VAR_client_id       = credentials('AZURE_CLIENT_ID')
        TF_VAR_client_secret   = credentials('AZURE_CLIENT_SECRET')
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
