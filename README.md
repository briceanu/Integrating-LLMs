🧠 FastAPI + OpenAI Chat Assistant

This project is a chat assistant built with FastAPI (backend), React (frontend), and OpenAI’s API.
Users can ask questions via a React client, which are sent to the FastAPI backend.
The backend forwards the question to OpenAI’s GPT model and returns the generated response.

⚠️ Note:
This middleware was added just to demonstrate how to create a middleware in FastAPI.
In real-world deployments, client IP checks are usually handled by a reverse proxy server (e.g., Nginx, Traefik, HAProxy).
That way, invalid requests never even reach your FastAPI app — saving server resources and bandwidth.

🚀 Features

✅ FastAPI backend with clean API routes

✅ OpenAI GPT integration using the official SDK

✅ Frontend client (React) for interactive Q&A

✅ Typed responses with Pydantic schemas

✅ Environment variable support via .env

.
├── app/
│ ├── routers/
│ │ └── ask_ai.py # FastAPI route for AI Q&A
│ ├── app_logic.py # Logic for calling OpenAI
│ ├── schemas.py # Pydantic models for validation
│ └── **init**.py
├── frontend/
│ └── src/ChatBox.jsx # React chat component
├── .env # Environment variables (not committed)
├── requirements.txt # Backend dependencies
├── package.json # Frontend dependencies
└── README.md # Documentation

⚙️ Installation
1️⃣ Clone the repo
git clone https://github.com/your-username/fastapi-openai-chat.git
cd fastapi-openai-chat

2️⃣ Backend Setup (FastAPI)

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate # Linux / Mac
venv\Scripts\activate # Windows

pip install -r requirements.txt

Set up your .env file:

OPENAI_API_KEY=your_openai_api_key_here

Run the FastAPI backend:

uvicorn app.main:app --reload

API will be available at:
👉 http://localhost:8000/docs

3️⃣ Frontend Setup (React)

Go to the frontend folder:

cd frontend
npm install
npm run dev # or npm start

React app will be running on:
👉 http://localhost:5173 (if using Vite)
👉 http://localhost:3000 (if using CRA)

📡 API Endpoints
POST /ask-ai

Ask a question to the AI.

Query Parameters:

question (string, max 100 chars) → The question to send to the AI.
