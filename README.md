# 🏥 Hospital Policy RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** based chatbot that answers hospital policy-related questions using Large Language Models (LLMs) and semantic search.

This project demonstrates how to combine **document retrieval + LLM reasoning** to build accurate, context-aware AI systems.

---

## 🚀 Features

- 💬 Ask natural language questions about hospital policies  
- 📄 Retrieves relevant policy documents using vector search  
- 🧠 Generates context-aware answers using LLM  
- ❌ Reduces hallucination by grounding responses in real data  
- 🔐 Secure API key handling using environment variables  

---

## 🧠 Tech Stack

- **Language**: Python  
- **Frameworks**: LangChain  
- **LLM Providers**: OpenAI / Groq  
- **Vector Database**: FAISS / Chroma  
- **Embeddings**: OpenAI Embeddings / HuggingFace  
- **Environment Management**: python-dotenv  

---

## ⚙️ How It Works (RAG Pipeline)

1. User asks a question  
2. The question is passed to a **retriever**  
3. Relevant document chunks are fetched from the vector database  
4. Retrieved context + user query are sent to the LLM  
5. LLM generates a grounded, accurate response  

---

## 📂 Project Structure
