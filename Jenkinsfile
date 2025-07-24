pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    environment {
        OPENAI_API_KEY = credentials('openai-api-key')  // Store your OpenAI key in Jenkins credentials
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
                    echo "📦 Installing Embedchain and OpenAI..."
                    pip install --upgrade pip
                    pip install embedchain openai
                '''
            }
        }

        stage('Prepare Error Log File') {
            steps {
                sh '''
                    echo "📝 Preparing log file..."
                    cp sample_error_log.txt error_log.txt 
                '''
            }
        }

        stage('Run AI Summarizer') {
            steps {
                sh '''
                    echo "🤖 Running AI summarizer..."
                    python error_summarizer_agent.py
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
