import os
from embedchain import App

# ✅ Set your OpenAI API Key from Jenkins ENV
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# ✅ Custom LLM + Embedder config
config = {
    'llm': {
        'provider': 'openai',
        'config': {
            'model': 'gpt-3.5-turbo',
            'temperature': 0.3
        }
    },
    'embedder': {
        'provider': 'openai',
        'config': {
            'model': 'text-embedding-ada-002'
        }
    }
}

# ✅ Instantiate with config
app = App(config=config)

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

if _name_ == "_main_":
    summarize_error_logs()
