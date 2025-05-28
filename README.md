# Promtior AI Engineer Technical Test

## Overview

A RAG (Retrieval-Augmented Generation) chatbot built with LangChain and OpenAI GPT.

---

## Step-by-Step Setup Guide

This guide will help you set up and run the project locally using Docker or Poetry, and test the API using the built-in playground.

---

## 1. Set Up Environment Variables

Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your-openai-key-here
```

---

## 2. Build and Run with Docker

### Build the Docker image:

```bash
docker compose build
```

### Run the Docker container:

```bash
docker compose up -d
```

---

## 3. Run Locally with Poetry

### 3.1. Create a virtual environment and install Poetry & LangChain CLI

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

```bash
pip install poetry langchain-cli
```

### 3.2. Install project dependencies

```bash
poetry install --no-interaction --no-ansi
```

### 3.3. Run the server

```bash
langchain serve --port=8080
```

---

## 4. Test the API in the Playground

Once the server is running, open your browser and go to:

```
http://localhost:8080/promtior/playground
```

You can interact with the Promtior API directly from this playground interface.

---

## 5. Linting and Formatting

To check code style and linting:

```bash
poetry run flake8
```

To auto-format code:

```bash
poetry run black .
```

---

## Technologies Used

- **LangChain**: LLM application framework
- **FastAPI**: Web framework for APIs  
- **OpenAI GPT**: Language model
- **Docker**: Containerization

