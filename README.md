# CloudPilot

[Demo](#) | ![MIT](https://img.shields.io/badge/License-MIT-green.svg) | Tech: GPT-4 | LangChain | Streamlit | AWS (Mock)

---

## Overview

**CloudPilot** is an AI-powered DevOps assistant that enables users to manage and simulate cloud infrastructure via natural language. By interpreting commands like “Deploy a web server in Mumbai with Python and Nginx,” CloudPilot generates safe execution plans, evaluates potential risks, and simulates cloud actions.

Built using **LangChain**, **GPT-4**, and mocked **AWS SDK**, CloudPilot showcases how AI agents can replace traditional IaC (Infrastructure as Code) with conversational workflows.

---

## Features

- 💬 Natural language to infrastructure translation  
- 🔐 Risk evaluation for sensitive/destructive ops  
- ⚙️ Agent routing and tool execution via LangChain  
- 🧪 boto3-mocked simulation (no real billing)  
- 🌐 Streamlit frontend for easy testing  

---

## Tech Stack

- GPT-4 via LangChain  
- Python + Streamlit  
- Simulated AWS SDK via boto3/moto  
- JSON output for infrastructure plans and logs  
