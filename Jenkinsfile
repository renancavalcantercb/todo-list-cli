pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('pypi_token')
    }

    parameters {
        string(name: 'NEW_VERSION', description: 'New version number (e.g., 0.6.0)')
        choice(name: 'VERSION_PART', choices: ['patch', 'minor', 'major'], description: 'Choose which part of the version to bump')
    }

    stages {
        stage('Cleanup') {
            steps {
                script {
                    sh 'rm -rf dist/*'
                    sh 'rm -rf build/*'
                    sh 'rm -rf *.egg-info'
                }
            }
        }

        stage('Set Version') {
            steps {
                script {
                    sh "sed -i 's/@VERSION/${NEW_VERSION}/g' setup.py"
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

