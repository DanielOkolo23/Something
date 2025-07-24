#!/bin/bash

# Navigate to the directory where this script is located
cd "$(dirname "$0")"

# Activate the virtual environment
source /var/lib/jenkins/jenkins_embedchain/venv/bin/activate

# Run the summarizer script
python3 error_summarizer_agent.py
