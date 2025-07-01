# end-to-end-data-science-project

NAME : AKSHAY A

INTERN ID : CT04DF2711

DOMAIN : DATA SCIENCE

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

# 📊 End-to-End Data Science Project: Customer Churn Prediction

This project demonstrates a complete end-to-end data science workflow — from data preprocessing and feature engineering to model training, evaluation, and deployment using a Flask API.

---

## 🎯 Objective

Predict whether a customer will churn (leave a service) based on their behavior and profile data, and expose the prediction model via a web API.

---

## 🚀 Workflow Overview

1. *Data Collection* – Load historical customer data (CSV)
2. *Exploratory Data Analysis (EDA)* – Understand data distributions and correlations
3. *Data Preprocessing* – Clean missing values, encode categories, scale features
4. *Model Building* – Train a machine learning model (e.g., Logistic Regression, Random Forest)
5. *Model Evaluation* – Evaluate accuracy, precision, recall, and confusion matrix
6. *Model Serialization* – Save trained model using pickle
7. *Model Deployment* – Deploy as a REST API using Flask

---

## 🛠 Tech Stack

- Python 3.x
- pandas, numpy, matplotlib, seaborn
- scikit-learn – for machine learning and preprocessing
- Flask – for model deployment
- pickle – to save the trained model

---

## 📁 Project Structure

| File/Folder            | Description                                        |
|------------------------|----------------------------------------------------|
| data/                | Raw CSV files used for training                    |
| notebooks/EDA.ipynb  | Exploratory Data Analysis                          |
| src/preprocessing.py | Data preprocessing functions                       |
| train_model.py       | Script to train and save the model                 |
| model.pkl            | Saved machine learning model                       |
| app.py               | Flask API for predictions                          |
| requirements.txt     | Required Python packages                           |
| README.md            | Project overview and usage instructions            |

---
