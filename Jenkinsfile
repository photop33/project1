pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/photop33/project1.git'
            }
        }
        stage('web_app') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\web_app.py'
                    bat 'echp success'
                }
            }
        }
        stage('rest_app') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\rest_app.py'
                }
            }
        }
        stage('test-rest_app') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\test-rest_app.py'
                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\Backend_testing.py'
                }
            }
        }
        stage('frontend_testing.py') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\frontend_testing.py'
                }
            }
        }
        stage('combined_testing') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\combined_testing.py'
                }
            }
        }
        stage('frontend_testing') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\clean_environment.py'
                    bat 'echo success'              
                }
            }
        }      
        stage('Test') {  
            steps {  
                bat 'echo "Fail!"; exit 1'  
            }  
        }  
    }
    post {  
        always {  
            echo 'This will always run'  
        }  
        success {  
            echo 'This will run only if successful'  
        }  
        failure {  
            mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "foo@foomail.com";  
        }  
        unstable {  
            echo 'This will run only if the run was marked as unstable'  
        }  
        changed {  
            echo 'This will run only if the state of the Pipeline has changed'  
            echo 'For example, if the Pipeline was previously failing but is now successful'  
        }  
    }  
}
    
node {
  properties(
    [
        parameters(
            [
                string(defaultValue: 'swisalior', name: 'Username'),
                print ( "DEBUG: parameter foo = ${env.Username}")

            

    ]
    )    
  ]
  )
}

