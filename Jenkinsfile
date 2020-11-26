pipeline {
  options {timestamps()}
  agent none
  stages {
    stage('Check scm') {
    agent any 
    steps {
      checkout scm
    }
  }// stage Build
  stage('Build') { 
    steps {
      echo "Building ...${BUILD_NUMBER}"
      echo "Build completed"
    }
  }// stage Build
  stage('Test') {
      agent { docker {image 'alpine'
      args '-u=\"root\"'
    }
  }
  steps {
    sh 'apk add python3 py-pip'
    sh 'apk add docker'
    sh 'apk add python3'
    sh 'pip install Flask'
    sh 'pip install xmlrunner'
    sh 'python3 TestMe.py'
  }
  post{ 
    always {
      junit 'test-reports/*.xml'
    }
    success {
      echo "Application testing successfully completed "
      sh 'docker build .'
    }
    failure {
      echo "Oooppss!!! Tests failed!"
    }
  } // post
  }// stage Test
    stage('Docker Publish')
		{
            agent any
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo "Application Publishing"
                checkout scm
                script {
                    def customImage = docker.build("docker-test:${env.BUILD_ID}")
                    //docker.withRegistry('',registryCredential )
                    //{
                    //    customImage.push()}
                    //}

            }
  } // stages
}
