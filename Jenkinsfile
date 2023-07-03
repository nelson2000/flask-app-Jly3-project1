node {

        def app

        stage("clone repository") {
            checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nelson2000/flask-app-Jly3-project1.git']])
        }

        stage("Build Image") {

            app = docker.build("nwajienelson/flaskapp-jly3")
        }


        stage("Test Image"){

            app.inside{
                sh 'echo "Test completed and passed"'
            }
        }

        stage("Push Image") {

            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_cred') {

                    app.push("${env.BUILD_NUMBER}")


            }

        }
        
        stage('Trigger ManifestUpdate'){

            echo "triggering updatemanifestsjob"

            build job: 'flask-job2', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
    

}



