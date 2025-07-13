🦠 COVID-19 Prediction Web Application

A web-based machine learning application that predicts the likelihood of COVID-19 infection based on user-reported symptoms and exposure history. Built using Streamlit, FastAPI, and ML models (XGBoost, Random Forest, Logistic Regression).

-------------------------------------------------------------------

🔍 Features

Real-time prediction of COVID-19 status

Interactive frontend built with Streamlit

Backend API powered by FastAPI

Trained ML models using Scikit-learn, XGBoost

Model performance tracked with MLflow

Deployed with Docker for easy hosting

-------------------------------------------------------------------


🧠 Machine Learning

Preprocessed data from Kaggle Dataset

Tried multiple models: Logistic Regression, Random Forest, XGBoost

Selected XGBoost with best performance (F1-score: 0.95)

Trained with class balancing and hyperparameter tuning

-------------------------------------------------------------------

🚀 How to Run Locally

Requirements

pip install -r requirements.txt


Start Backend

cd api/

uvicorn main:app --reload


Start Frontend

streamlit run frontend/app.py

