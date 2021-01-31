pipeline {
    agent any
    stages {
        stage('Setup parameters') {
            steps {
                script { 
                    properties([
                        parameters([
                            string(
                                defaultValue: '1', 
                                name: 'STRING-PARAMETER', 
                                Description: 
                                 script {
                                     git 'https://github.com/photop33/project1.git'
                                 }
                            ),
                               string(
                                defaultValue: '2', 
                                name: 'STRING-PARAMETER', 
                                Description: 
                                 script {
                                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\web_app.py'
                                    bat 'echo success'
                                 }
                                 
                             ),
                               string(
                                defaultValue: '3', 
                                name: 'STRING-PARAMETER', 
                                Description: 
                                 script {
                                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\rest_app.py'
                                    bat 'echo success'
                                 }
                                 
                            ),
                               string(
                                defaultValue: '4', 
                                name: 'STRING-PARAMETER', 
                                Description: 
                                 script {
                                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\test-rest_app.py'
                                    bat 'echo success'
                            })
                        ])
                    ])
                }
            }
        }
    }
}
 
