pipeline {
    agent any

    environment {
        // Replace with your real OpenAI secret name in Jenkins credentials store
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install embedchain openai
                '''
            }
        }

        stage('Simulate Error Logs') {
            steps {
                sh 'cp sample_error_log.txt error_log.txt'
            }
        }

        stage('Run AI Error Summarizer') {
            steps {
                sh 'python error_summarizer_agent.py'
            }
        }

        stage('Publish AI Summary') {
            steps {
                sh '''
                    echo "===== AI-Generated Summary ====="
                    cat error_summary.md
                    echo "================================="
                '''
            }
        }
    }
}
