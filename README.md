# 🏏 IPL Match Prediction & Analytics System

A full-stack AI-powered platform that predicts IPL match outcomes and provides insightful player and team analytics using machine learning, live data scraping, and LLM-based reasoning.

---

## 📌 Features

### 🔍 Machine Learning & Prediction
- Ensemble model combining Gradient Boosting and Neural Networks
- Predictions include:
  - Match Winner
  - Final Scores (Winner & Loser)
  - Key Player Metrics (Runs, Wickets, Economy)
- Time-series trend analysis over last 3–5 matches
- Confidence intervals for predictions

### 🤖 LLM-Based Reasoning
- Integration with **Ollama** for local LLM inference
- Natural language explanations of model predictions
- Prompt engineering layer for high-quality insights

### 🔧 Backend
- Django backend with REST API (via Django REST Framework)
- FastAPI service to serve lightweight ML inference
- JWT-based authentication
- Swagger/OpenAPI documentation

### 🌐 Frontend
- React.js dashboard for:
  - Live match updates
  - Interactive prediction and analysis
  - Player performance visualizations
  - Chatbot interface powered by the LLM

### 📊 Data Pipeline
- Selenium-based scrapers for:
  - Match data
  - Player statistics
  - Real-time updates during live games
- Data validation, normalization, and transformation pipeline
- Automatic model retraining support

---


## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/ipl-prediction-project.git
cd ipl-prediction-project

### 2. Set Up Python Environment

python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux

pip install --upgrade pip
pip install -r requirements.txt
### 3. Configure Environment Variables
Rename .env.example to .env and fill in required keys (database, API tokens, etc.).

### 4. Start Django Backend

cd backend/django_app
python manage.py migrate
python manage.py runserver

### 5. Start FastAPI Microservice

cd ../fastapi_service
uvicorn main:app --reload

### 6. Start React Frontend

cd frontend
npm install
npm start

## 🧠 LLM Setup (Ollama)
Ensure you have Ollama installed and running locally.

ollama run llama3
The backend will connect to the local LLM server at http://localhost:11434.

## 📈 Model Training
To retrain the model with new data:

cd backend/models
python train_model.py
You can automate retraining via a cron job or scheduler (included in the scraper/).

## 📬 API Documentation
Visit:

Swagger UI: http://localhost:8000/api/docs/

Redoc: http://localhost:8000/api/redoc/

## 🛠 Special Instructions
Use Postman collection ipl-api.postman_collection.json for testing endpoints.

If using Docker, refer to docker/README.md for full containerized setup.

Frontend auto-refreshes with WebSocket-based live updates during matches.

## 🧑‍💻 Author & Contact
Sachit Panda
Email: sachitpanda17@gmail.com
Phone: +91-9348872307
GitHub: github.com/dark-eternal
LinkedIn: linkedin.com/in/sachit-panda
