
# 🧠 Viral Tweet Reflector

Improve your tweets with AI-powered feedback and rewriting to make them more viral, clear, and stylish. This project leverages the power of LangGraph for intelligent agent orchestration, FastAPI for a robust backend API, and Streamlit for an interactive web interface. 

--- 

## ✨ Features

- **AI-Powered Tweet Generation**: Generate highly engaging and concise tweets from your input.
- **Iterative Reflection & Improvement**: The agent self-critiques and refines tweets based on predefined criteria for virality, clarity, and style.
- **Detailed Feedback**: Get actionable insights on why a tweet was rewritten and how it can be further improved.
- **Interactive Web Interface**: A user-friendly Streamlit application to submit tweets and view results.
- **Scalable Backend**: Built with FastAPI, ready for deployment.

---

## 🚀 How It Works

The Viral Tweet Reflector operates as a multi-step AI agent:

1. **Tweet Generation**: An initial tweet is generated based on your input, aiming for virality and impact.
2. **Self-Reflection**: An "influencer" AI reflects on the generated tweet, providing detailed critique on its hook, conciseness, value, engagement, tone, hashtags, and emojis.
3. **Decision Loop**: Based on the reflection, the agent decides if the tweet is "good enough" (e.g., received a high grade/score) or if it needs further refinement.
4. **Iterative Refinement**: If refinement is needed, the process loops back to generation, where the AI attempts to improve the tweet incorporating the previous feedback. This continues until the tweet meets the virality criteria or a set limit of iterations is reached.

---

## 🛠️ Technologies Used

- **LangGraph**: For building robust, stateful AI agents with iterative loops.
- **LangChain**: Core framework for working with large language models.
- **Groq**: Provides fast and efficient inference for the llama3-8b-8192 language model.
- **FastAPI**: A modern, fast (high-performance) web framework for building the API backend.
- **Pydantic**: For data validation with FastAPI.
- **Streamlit**: For creating the interactive and user-friendly web interface.
- **Python-dotenv**: For managing environment variables.
- **Black & iSort**: For code formatting and import organization.

---

## 📂 Project Structure

```
viral-tweet-agent/
├── .env
├── requirements.txt
├── streamlit/
│   └── app.py
├── scripts/
│   ├── run_agent.py
│   └── evaluate_agent.py
└── src/
    ├── __init__.py
    ├── agents/
    │   ├── __init__.py
    │   ├── nodes.py
    │   └── twitter_agent.py
    ├── config.py
    ├── services/
    │   ├── __init__.py
    │   └── api.py
    └── utils/
        ├── __init__.py
        └── prompt_templates.py
```
---

## ⚡ Setup and Local Installation

Follow these steps to get the Viral Tweet Reflector up and running on your local machine.

### Prerequisites

- Python 3.10+
- A Groq API Key (you can get one from Groq Console)

### 1. Clone the Repository

```bash
git clone https://github.com/Saketh-Vadlamudi/Viral-Tweet-Reflector.git
cd Viral-Tweet-Reflector
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
# On Linux/macOS
source env/bin/activate
# On Windows
.\env\Scriptsctivate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of your project (`viral-tweet-agent/`) and add:

```ini
# .env file
GROQ_API_KEY="YOUR_GROQ_API_KEY_HERE"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="reflection-agent"
LANGCHAIN_API_KEY="YOUR_LANGCHAIN_API_KEY_HERE" # Optional
```

### 5. Run the Backend API

```bash
uvicorn src.services.api:app --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to check the API.

### 6. Run the Streamlit Frontend

In a new terminal:

```bash
streamlit run streamlit_app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧪 Testing the Agent (Command Line)

```bash
python scripts/run_agent.py
# Or
python scripts/evaluate_agent.py
```

Evaluation results will be saved to `eval_results.json`.

---

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a PR to improve performance, UI, or features.

---
