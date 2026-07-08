# Suvidha AI 🤖

A conversational chatbot built with **LangChain** and **LangGraph**, using **Retrieval-Augmented Generation (RAG)** to answer questions grounded in your own documents. Supports multiple LLM providers so you can swap models without rewriting your pipeline.

## ✨ Features

- 🔍 **Retrieval-Augmented Generation** — answers are grounded in retrieved context, not just model memory
- 🧠 **Multi-LLM support** — Google Gemini, Groq, Mistral, DeepSeek, and Hugging Face models
- 📦 **Vector search** with FAISS for fast, local similarity search
- 🔗 **LangGraph** for structured, stateful conversation flows
- ⚡ **FastAPI** backend for serving the chatbot as an API

## 🛠️ Tech Stack

| Component        | Technology                          |
|-------------------|--------------------------------------|
| Orchestration     | LangChain, LangGraph                |
| Vector Store      | FAISS                               |
| LLM Providers     | Google Gemini, Groq, Mistral, DeepSeek, Hugging Face |
| Tokenization      | tiktoken                            |
| API Framework     | FastAPI + Uvicorn                   |
| Config            | python-dotenv                       |

## 📁 Project Structure

```
.
├── app.py                # Main application entry point
├── requirements.txt      # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sarthak1979/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

```
GOOGLE_API_KEY=your_key_here
DEEPSEEK_API_KEY=your_key_here
HUGGINGFACEHUB_ACCESS_TOKEN=your_key_here
MISTRAL_API_KEY=your_key_here
```

> ⚠️ Never commit your `.env` file — it's already excluded via `.gitignore`.

### 5. Run the app

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Suvidha AI is now ready to answer questions grounded in your documents. 🎉

## 📖 How It Works

1. Documents are loaded and split into chunks
2. Chunks are embedded and stored in a FAISS vector index
3. On each user query, relevant chunks are retrieved from FAISS
4. The retrieved context + query are passed to the selected LLM
5. LangGraph manages the conversation state and flow
6. The chatbot returns a grounded, context-aware response

## 🗺️ Roadmap

- [ ] Add support for PDF/CSV document ingestion
- [ ] Add streaming responses
- [ ] Add conversation memory persistence
- [ ] Deploy with Docker

## 📄 License

This project is licensed under the MIT License.
