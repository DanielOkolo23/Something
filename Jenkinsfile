pipeline {
    agent any

    environment {
        // 🔐 Make sure these are securely stored in Jenkins Credentials
        OPENAI_API_KEY = credentials('openai-api-key')        // Your OpenAI token
        SUDO_PASSWORD  = credentials('sudo-password')         // Your system user sudo password
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Python & Pip') {
            steps {
                sh '''
                    echo "🔧 Installing Python, pip, and venv..."
                    echo "$SUDO_PASSWORD" | sudo -S apt-get update -y
                    echo "$SUDO_PASSWORD" | sudo -S apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                    echo "🐍 Creating virtual environment..."
                    python3 -m venv venv

                    echo "📦 Installing dependencies..."
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install embedchain openai
                '''
            }
        }

        stage('Prepare Error Log') {
            steps {
                sh '''
                    echo "📝 Copying sample error log..."
                    cp sample_error_log.txt error_log.txt 
                '''
            }
        }

        stage('Run AI Summarizer') {
            steps {
                sh '''
                    echo "🤖 Running AI summarizer..."
                    . venv/bin/activate
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
