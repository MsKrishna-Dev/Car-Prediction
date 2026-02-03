# 🚗 Car Price Prediction System

A full-stack machine learning project that predicts the selling price of a car based on its features using a trained ML model, exposed via a FastAPI backend and consumed through a Streamlit frontend UI.

This project demonstrates:
- End-to-end ML pipeline
- Model deployment using FastAPI
- Frontend integration using Streamlit
- Real-world API consumption

---

## 🔥 Live Demo

👉 (Add your deployed Streamlit link here)

---

## 📌 Features

- 📊 Predicts car selling price in real-time
- ⚡ FastAPI backend for fast inference
- 🖥 Interactive Streamlit web interface
- 📦 Pre-trained ML model using Scikit-learn
- 🔁 REST API communication

---

## 🏗 Project Architecture

```
Car Price FastAPI/
│
├── model/
│ ├── car_price_model.pkl
│ └── encoder.pkl
│
├── main.py # FastAPI backend
├── schema.py # Pydantic request schema
├── streamlit_app.py # Streamlit frontend
├── requirements.txt
├── README.md
└── .gitignore

```

---

## 🛠 Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| ML | Scikit-learn |
| Data | Pandas, NumPy |
| Deployment | Render, Streamlit Cloud |

---

## 📊 Input Features

| Feature        | Description                                   |
|----------------|-----------------------------------------------|
| Car_Name       | Name of the car                               |
| Year           | Manufacturing year                            |
| Present_Price  | Current showroom price (in lakhs)             |
| Kms_Driven     | Total kilometers driven                       |
| Fuel_Type      | Petrol / Diesel / CNG                         |
| Seller_Type    | Dealer / Individual                           |
| Transmission   | Manual / Automatic                            |
| Owner          | 0 = First owner, 1 = Second owner, 3 = Third owner |

---

## 🚀 How It Works

1. User enters car details in the Streamlit UI
2. UI sends a POST request to the FastAPI /predict endpoint
3. Backend loads the trained ML model
4. Model predicts the car selling price
5. Result is returned and displayed in the UI

---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
- git clone https://github.com/your-username/car-prediction.git
cd car-prediction

2️⃣ Create Virtual Environment
- python -m venv venv
- source venv/bin/activate    # Linux/Mac
- venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
- pip install -r requirements.txt

4️⃣ Run FastAPI Backend
- uvicorn main:app --reload
- API will run at: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

5️⃣ Run Streamlit Frontend
- streamlit run streamlit_app.py
- App will open at: http://localhost:8501

---

