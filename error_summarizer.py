pipeline {
    agent any

    environment {
        // Store your OpenAI API key in Jenkins as a secret text credential named 'openai-api-key'
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install embedchain openai
                '''
            }
        }

        stage('Prepare Error Log File') {
            steps {
                sh '''
                    cp sample_error_log.txt error_log.txt 
                '''
            }
        }

        stage('Run AI Error Summarizer') {
            steps {
                sh '''
                    . venv/bin/activate
                    python error_summarizer_agent.py
                '''
            }
        }

        stage('Publish Error Summary') {
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
   
