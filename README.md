# Breast Cancer Predictor: AI-Powered Diagnostic Approach

## Overview

This project presents an AI-based diagnostic Approach for predicting breast cancer using machine learning techniques. It classifies tumors as benign or malignant based on cell nuclei features derived from medical data.

The system is designed to assist in early detection and provide a reliable, data-driven approach to support medical decision-making.

---

## Problem Statement

Breast cancer is one of the most common and life-threatening diseases worldwide. Early and accurate diagnosis is essential for effective treatment and improved survival rates.

Traditional diagnostic methods can be time-consuming, expensive, and sometimes inaccessible. This project aims to develop a machine learning-based system that provides quick and standardized predictions to assist healthcare professionals.

---

## Methodology

### Data Source

* Breast Cancer Wisconsin Dataset (scikit-learn)

### Data Preprocessing

* Conversion into structured format using Pandas
* Feature scaling using StandardScaler to normalize data

### Model Development

* Algorithm: Logistic Regression
* Train-test split: 80% training, 20% testing
* Model trained on scaled feature set

### Evaluation

* Model performance evaluated using accuracy on unseen test data

### Model Deployment

* Model and scaler saved using Pickle (`model.pkl`, `scaler.pkl`)
* Web application built using Streamlit for real-time predictions

---

## Core Functionalities

* Input of medical feature values
* Real-time prediction of tumor type (benign or malignant)
* Simple and interactive web interface
* Efficient and fast prediction system

---

## Results

The model achieves high accuracy in classifying tumors and provides consistent predictions on test data.


---


## How to Run

1. Clone the repository
   git clone https://github.com/arshjabbal-tech/Unimodal_Sentiment_Analysis.git

2. Navigate to the directory
   cd Unimodal_Sentiment_Analysis

3. Install dependencies
   pip install -r requirements.txt

4. Train the model
   python train_model.py

5. Run the web application
   streamlit run web_app.py

---

## Future Scope

* Integration with healthcare systems (EHR)
* Use of advanced models for improved accuracy
* Deployment as a cloud-based diagnostic tool
* Enhanced visualization and analytics

---

## Conclusion

This project demonstrates how machine learning can be effectively applied to healthcare for early breast cancer detection. It provides a reliable, efficient, and accessible tool that can assist in clinical decision-making while reducing dependency on traditional diagnostic methods.

