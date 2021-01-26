Started by user lior swisa
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in C:\Users\l1313\.jenkins\workspace\Test_Project
[Pipeline] {
[Pipeline] stage
[Pipeline] { (checkout)
[Pipeline] script
[Pipeline] {
[Pipeline] properties
[Pipeline] properties
[Pipeline] }
[Pipeline] // script
[Pipeline] git
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git.exe rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/Dgotlieb/JenkinsTest.git # timeout=10
Fetching upstream changes from https://github.com/Dgotlieb/JenkinsTest.git
 > git.exe --version # timeout=10
 > git --version # 'git version 2.30.0.windows.2'
 > git.exe fetch --tags --force --progress -- https://github.com/Dgotlieb/JenkinsTest.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision 043d8c8413a4c57eb7ac29378e2ad1c2ee20ba9d (refs/remotes/origin/master)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f 043d8c8413a4c57eb7ac29378e2ad1c2ee20ba9d # timeout=10
 > git.exe branch -a -v --no-abbrev # timeout=10
 > git.exe branch -D master # timeout=10
 > git.exe checkout -b master 043d8c8413a4c57eb7ac29378e2ad1c2ee20ba9d # timeout=10
Commit message: "Update 1.py"
 > git.exe rev-list --no-walk 043d8c8413a4c57eb7ac29378e2ad1c2ee20ba9d # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (test)
[Pipeline] script
[Pipeline] {
[Pipeline] bat

C:\Users\l1313\.jenkins\workspace\Test_Project>start/min python3 C:\Users\l1313\PycharmProjects\project1\res1_app.py
[Pipeline] bat

C:\Users\l1313\.jenkins\workspace\Test_Project>start/min python3 C:\Users\l1313\PycharmProjects\project1\web_app.py
[Pipeline] bat

C:\Users\l1313\.jenkins\workspace\Test_Project>start/min python3 C:\Users\l1313\PycharmProjects\project1\test-rest_app.py
[Pipeline] bat

C:\Users\l1313\.jenkins\workspace\Test_Project>start/min python3 C:\Users\l1313\PycharmProjects\project1\Backend_testing.py
[Pipeline] bat

C:\Users\l1313\.jenkins\workspace\Test_Project>python3 C:\Users\l1313\PycharmProjects\project1\frontend_testing.py
Traceback (most recent call last):
  File "C:\Users\l1313\PycharmProjects\project1\frontend_testing.py", line 11, in <module>
    user_name("1")
  File "C:\Users\l1313\PycharmProjects\project1\frontend_testing.py", line 7, in user_name
    driver.get("http://127.0.0.1:5000/user/" + a + "")
  File "C:\Users\l1313\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\selenium\webdriver\remote\webdriver.py", line 333, in get
    self.execute(Command.GET, {'url': url})
  File "C:\Users\l1313\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\l1313\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: net::ERR_CONNECTION_REFUSED
  (Session info: chrome=87.0.4280.141)

[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)
Stage "Test" skipped due to earlier failure(s)
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
This will always run
[Pipeline] mail
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: script returned exit code 1
Finished: FAILURE








Script pipline
pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/Dgotlieb/JenkinsTest.git'
            }
        }
        stage('test') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\res1_app.py'
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\web_app.py'
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\test-rest_app.py'
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\project1\\Backend_testing.py'
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\frontend_testing.py'
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\project1\\combined_testing.py'
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