pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS')
        disableConcurrentBuilds()
    }
    stages {
        stage("init") {
            agent any
            steps { init() }
        }
        stage("buildECRCotainer") {
            agent any
            steps {
                sh 'docker build -t "app_python_$BRANCH_NAME" --no-cache -f $WORKSPACE/Dockerfile .'
            }
        }
        stage('cleanUpImage') {
            agent any
            steps {
                sh 'docker rmi app_python_$BRANCH_NAME'
            }
        }
    }
}

def init(){
    String base_uri  = '590183952025.dkr.ecr.us-east-2.amazonaws.com'
    String repository = base_uri + '/api-python'
    String tag = env.BRANCH_NAME + '_' + env.BUILD_NUMBER
    env.ECR_IMAGE_URI = repository
    env.TAG = tag
}