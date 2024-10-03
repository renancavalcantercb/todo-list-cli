pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('pypi_token')
    }

    parameters {
        string(name: 'VERSION_TAG', defaultValue: 'patch', description: 'Bump version (patch, minor, major)')
    }

    stages {
        stage('Bump Version') {
            steps {
                script {
                    sh "bump2version ${VERSION_TAG}"
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

