pipeline
{
    environment {
        registryCredential = '343757d8-42b8-4283-a65c-e4b3bb8a6ab2'
        dockerImage = ''
    }
	options
	{
		timestamps()
	}
	agent none
	stages
	{
		stage('Check scm')
		{
			agent any
			steps
			{
				checkout scm
			}
		} // stage Build
		stage('Build')
		{
			steps
			{
				echo "Building ...${BUILD_NUMBER}"
				echo "Build completed"
			}
		} // stage Build
		stage('Test')
		{
			agent
			{
				docker
				{
					image 'alpine'
					args '-u=\"root\"'
				}
			}
			steps
			{
			    sh 'apk add python3 py-pip'
			    sh 'pip install Flask'
			    sh 'pip install xmlrunner'
			    sh 'python3 TestMe.py'
			}
			post
			{
				always
				{
					junit 'test-reports/*.xml'
				}
				success
				{
					echo "Application testing successfully completed "
				}
				failure
				{
					echo "Oooppss!!! Tests failed!"
				}
			} // post
		} // stage Test
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
                    def customImage = docker.build("storminside4766/proga_lab_2:${env.BUILD_ID}")
                    docker.withRegistry('',registryCredential )
                    {
                        customImage.push()
                    }
                }
            }
		} // stage Build
	} // stages
}

