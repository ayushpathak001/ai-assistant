# 🍯 HoneyAssist AI — Backend

FastAPI backend for **HoneyAssist**, an AI-powered assistant developed as part of the **Honey Chain** project for the Smart India Hackathon (SIH).

HoneyAssist uses **NVIDIA's OpenAI-compatible API with the `openai/gpt-oss-20b` model** to answer beekeeper questions using structured beekeeper, honey batch, hive health, honey quality, IoT, blockchain, and beekeeping knowledge provided through the system instructions.

## 🚀 Features

* ⚡ FastAPI-based REST API
* 🤖 AI-powered beekeeper assistant
* 🧠 Context-aware conversations
* 👤 Multiple demo beekeeper profiles
* 🍯 Honey batch information
* 🐝 Hive and colony health information
* 💧 Honey moisture and quality information
* 📦 Batch traceability concepts
* 🔗 Blockchain and IoT awareness
* 💬 Conversational question answering
* 🔑 NVIDIA API integration
* 🗂️ In-memory conversation sessions for the current prototype

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **OpenAI Python SDK**
* **NVIDIA API**
* **GPT-OSS 20B**
* **Pydantic**
* **python-dotenv**
* **Uvicorn**

## 🔌 API

### `POST /ai/chat`

Example request:

```json
{
  "user_id": "ayush01",
  "message": "How much honey do I have?"
}
```

Example response:

```json
{
  "user_id": "ayush01",
  "response": "You currently have 26.4 kg of honey in batch BATCH004."
}
```

## 🧪 Current Prototype

The current version uses **demo beekeeper data and in-memory sessions**. MongoDB, OAuth2/JWT authentication, and production database integration are intentionally kept out of this prototype.

These components can be integrated in a later version when the Honey Chain platform is connected to real beekeeper and IoT data.

## 🎯 Project Goal

HoneyAssist is designed to provide beekeepers with a simple conversational interface where they can ask questions about their **honey production, batch information, hive health, honey quality, IoT readings, and traceability** without needing to manually search through different systems.

Part of the **Honey Chain — SIH Project**.
