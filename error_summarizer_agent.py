import os
from embedchain import App

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Simpler default initialization
app = App()

def summarize_error_logs():
    with open("error_log.txt", "r") as f:
        logs = f.read()

    prompt = f"""You are an expert log analyst. Analyze the following server error log and provide a summary with:
- Major issues
- Common errors
- Any repeated patterns

Log:
{logs}
"""
    result = app.query(prompt)

    with open("error_summary.md", "w") as f:
        f.write(result)

    print("✅ Error summary generated.")

if __name__ == "__main__":
    summarize_error_logs()
