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

        stage('Run AI Summarizer (via venv)') {
            steps {
                sh '''
                    echo "📦 Activating virtual environment and running summarizer..."
                    bash -c 'cd "$WORKSPACE" && source /var/lib/jenkins/jenkins_embedchain/venv/bin/activate && python3 error_summarizer_agent.py'
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
