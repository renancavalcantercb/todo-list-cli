pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('pypi_token')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python setup.py sdist bdist_wheel'
                }
            }
        }

        stage('Upload to PyPI') {
            steps {
                script {
                    sh 'pip install twine'

                    sh 'twine upload dist/* -u __token__ -p $PYPI_TOKEN'
                }
            }
        }
    }
}

