pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('pypi_token')
    }

    parameters {
        string(name: 'VERSION_NUMBER', description: 'Version number to bump to')
    }

    stages {
        stage('Set Version') {
            steps {
                script {
                    sh "bump2version --new-version ${VERSION_NUMBER} --allow-dirty --no-tag --commit"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python3 setup.py sdist bdist_wheel'
                }
            }
        }

        stage('Upload to PyPI') {
            steps {
                script {
                    sh 'pip3 install twine'

                    sh 'twine upload dist/* -u __token__ -p $PYPI_TOKEN'
                }
            }
        }
    }
}

