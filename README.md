# CloudPrompt

[Demo](#) | ![MIT](https://img.shields.io/badge/License-MIT-green.svg) | Tech: GPT-4 | LangChain | Streamlit | Python | Mock AWS

---

## Overview

**CloudPrompt** is an LLM-powered DevOps assistant that translates natural language into simulated cloud infrastructure actions. Instead of writing Terraform or navigating AWS dashboards, users can say things like:

> “Spin up a t3.micro EC2 instance in ap-south-1 with Python and nginx.”

It will parse the intent, simulate execution via mocked AWS APIs (boto3), and return logs, cost estimates, and risk warnings.

Built using **LangChain**, **GPT-4**, and **Streamlit**, CloudPrompt is designed to show how AI agents can manage infrastructure safely and conversationally.

---

## Features

- 💬 Converts natural language into structured infra actions
- 🔒 Risk evaluation for destructive commands (e.g., terminate)
- 🧠 Agent-tool integration using LangChain
- 📊 Simulated output: infra plan, cost, logs
- 🌐 UI built with Streamlit

---

## Tech Stack

- LangChain + OpenAI (GPT-4 or compatible)
- Python + Mocked boto3 via `moto`
- Streamlit interface
- JSON-based infra simulation

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/CloudPrompt.git
cd CloudPrompt
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run streamlit_app.py
```

> ✅ Simulated infra plan and logs will be displayed

---

## 🧠 Architecture

```
User Prompt → LangChain Agent → Simulated AWS Tool → Plan + Logs → Streamlit UI
```

📦 Tools: LangChain Agent | Simulated Boto3 Tool | JSON Plans  
🎯 Output: Execution Summary + Risk Flags + Cost Estimate

---

## 💡 Use Cases

- Rapid infra prototyping without real cloud billing
- DevOps education assistant
- LLM-powered agent toolchain showcase

---

## 🛣️ Roadmap

- [ ] Add AWS Pricing API for real-time cost estimates
- [ ] Real infra deployment toggle (with credentials)
- [ ] LangGraph agent loop
- [ ] Voice-to-infra via Whisper or Vapi

---

## 🧪 Sample Prompts

```
Spin up a t3.micro EC2 in ap-south-1 with Python and nginx
Destroy all EC2 instances in us-east-1
List my S3 buckets and show usage stats
```

---

## 🙏 Acknowledgements

Inspired by:
- LangChain + LLM Agents
- AWS Boto3 SDK
- AI-native DevOps tools like AutoInfra and Databricks Assistant
