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
        stage("pushToECRRepository") {
            agent any
            steps {
                sh 'aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $BASE_URI'
                sh 'docker tag app_python_$BRANCH_NAME:latest $ECR_IMAGE_URI'
                sh 'docker push $ECR_IMAGE_URI'
            }
        }
        stage("deploy") {
            agent any
            steps {
                sh 'docker run -d -p 8000 $ECR_IMAGE_URI'
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
    env.BASE_URI = base_uri
    env.ECR_IMAGE_URI = repository
    env.TAG = tag
}