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

        stage('Install System Packages (Python & Pip)') {
            steps {
                sh '''
                    echo "🔧 Installing Python and pip..."
                    sudo apt-get update -y
                    sudo apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Set Up Python Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                    echo "🐍 Creating virtual environment..."
                    python3 -m venv venv

                    echo "📦 Activating and installing dependencies..."
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install embedchain openai
                '''
            }
        }

        stage('Prepare Error Log File') {
            steps {
                sh '''
                    echo "📝 Copying sample error log..."
                    cp sample_error_log.txt error_log.txt 
                '''
            }
        }

        stage('Run AI Error Summarizer') {
            steps {
                sh '''
                    echo "🤖 Running the AI summarizer script..."
                    . venv/bin/activate
                    python error_summarizer_agent.py
                '''
            }
        }

        stage('Publish Error Summary') {
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
