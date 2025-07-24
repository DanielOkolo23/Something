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

        stage('Prepare Error Log File') {
            steps {
                sh '''
                    echo "📝 Preparing log file..."
                    cp error_log_samples/sample_error_log.txt error_log.txt
                '''
            }
        }

        stage('Run AI Summarizer') {
            steps {
                sh '''
                    echo "🤖 Running AI summarizer..."
                    python3 error_summarizer_agent.py
                '''
            }
        }

        stage('Display AI Summary') {
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
