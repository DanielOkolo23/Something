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
                    echo "📝 Preparing error log file..."
                    cp sample_error_log.txt error_log.txt
                '''
            }
        }

        stage('Run AI Summarizer (via shell script)') {
            steps {
                sh '''
                    echo "✅ Making summarizer script executable..."
                    chmod +x run_summarizer.sh
                    echo "🤖 Running AI summarizer..."
                    bash run_summarizer.sh
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

