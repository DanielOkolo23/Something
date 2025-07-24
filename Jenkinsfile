pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Log') {
            steps {
                sh '''
                    cp sample_error_log.txt error_log.txt
                '''
            }
        }

        stage('Run AI Summarizer (via venv)') {
            steps {
                sh '''
                    echo "📦 Activating virtual environment and running summarizer..."
                    source ~/jenkins_embedchain/venv/bin/activate
                    python3 error_summarizer_agent.py
                '''
            }
        }

        stage('Show Summary') {
            steps {
                sh '''
                    echo "===== 🧠 AI-Generated Summary ====="
                    cat error_summary.md
                    echo "==================================="
                '''
            }
        }
    }
}
