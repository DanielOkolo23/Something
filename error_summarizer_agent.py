import os
from embedchain import App
from embedchain.config import AppConfig, OpenAIConfig, OpenAIEmbedderConfig

# Set your OpenAI API Key from environment (Jenkins)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# ✅ Define proper configuration using Embedchain's config classes
llm_config = OpenAIConfig(
    model="gpt-3.5-turbo",
    temperature=0.3
)

embedder_config = OpenAIEmbedderConfig(
    model="text-embedding-ada-002"
)

app_config = AppConfig(
    llm=llm_config,
    embedder=embedder_config
)

# ✅ Instantiate App with proper AppConfig
app = App(config=app_config)

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
