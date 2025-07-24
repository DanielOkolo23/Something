#!/bin/bash

# Get full path to script directory reliably
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

# Change to the directory where the script is located
cd "$SCRIPT_DIR" || exit 1

# Activate the virtual environment
source /var/lib/jenkins/jenkins_embedchain/venv/bin/activate

# List contents to verify file is there
echo "📁 Files in working directory:"
ls -l

# Run the Python script
python3 error_summarizer_agent.py
