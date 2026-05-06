# Drishti: Breast Cancer Predictor: AI-Powered Diagnostic Assistant

## Project Name: Drishti (दृष्टि)

"Drishti" means vision.  
This project represents the idea of detecting breast cancer at an early stage using machine learning, enabling timely diagnosis and better medical outcomes.

## Overview

This project, **Drishti**, presents an AI-based diagnostic assistant for predicting breast cancer using machine learning techniques. It classifies tumors as benign or malignant based on cell nuclei features derived from medical data.

The system is designed to assist in early detection and provide a reliable, data-driven approach to support decision-making.

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

* Model performance was evaluated using accuracy on unseen test data
* The model achieved an accuracy of 97.37% on the test dataset

### Model Deployment

* Model and scaler saved using Pickle (`model.pkl`, `scaler.pkl`)
* Web application built using Streamlit for real-time predictions

---

## Web Application Deployment

The web application for this project has been deployed using **Streamlit Cloud**.
It provides an interactive interface where users can input medical parameters and obtain real-time predictions for breast cancer classification.

**Live Application:**

[Open App](https://drishtibreastcancerpredictor.streamlit.app/)

---

## Feature-Based Prediction

The model uses 30 input features derived from cell nuclei characteristics, including:

* Size-related features (radius, perimeter, area)
* Texture-related features
* Shape-related features (concavity, symmetry, fractal dimension)

Each of these features contributes to the final classification by capturing different aspects of the tumor’s structure.

---

## Visualization

<img width="1470" height="884" alt="Screenshot 2026-04-26 at 6 57 51 PM" src="https://github.com/user-attachments/assets/8291fad1-ad41-4ef7-aa53-1e56bea729a2" />

---

## Prediction Confidence

The model provides a confidence score along with each prediction, indicating how certain it is about the result.

For example, a confidence score of 93.5% (Benign) means the model estimates a 93.5% probability that the tumor is non-cancerous.

### Why Confidence Matters

* Helps assess the reliability of the prediction
* Higher confidence (e.g., above 90%) suggests strong certainty
* Lower confidence indicates uncertainty and may require further medical evaluation

**Note:** Confidence does not guarantee correctness; it only reflects the model’s estimated probability.

---

## Radar Chart

A radar chart is used to provide a visual summary of the input features. The features are grouped into three categories:

1. Mean Features – Average values of the measurements
2. Error Features – Variation or standard error in the measurements
3. Worst Features – Maximum (extreme) values observed

### How to Interpret the Radar Chart

* Each axis represents Mean, Error, and Worst features
* The plotted area shows the relative magnitude of each category
* Values farther from the center indicate higher magnitudes

### What the Chart Represents

* Larger spread toward Worst features indicates more extreme values
* Higher Error values indicate greater variability
* Balanced distribution is often associated with benign cases

---
## Radar Chart Visualization

<img width="759" height="598" alt="Screenshot 2026-04-26 at 6 27 31 PM" src="https://github.com/user-attachments/assets/69c27fc3-5f4b-4adc-85ce-d726da6ddc6e" />

---

## Usage Instructions

1. Open the live application link
2. Enter the required feature values
3. Click on the prediction button
4. View the result (Benign or Malignant)

---

## Deployment Details

* Platform: Streamlit Cloud
* Backend Model: Logistic Regression (Scikit-learn)
* Model Serialization: Pickle (`model.pkl`, `scaler.pkl`)

---

## Core Functionalities

* Input of medical feature values
* Real-time prediction of tumor type
* Simple and interactive web interface
* Efficient and fast prediction system

---

## Results

The model achieves high accuracy in classifying tumors and provides consistent predictions on test data.

---

## How to Run

1. Clone the repository

   ```
   git clone https://github.com/arshjabbal-tech/Breast_Cancer_Predictor.git
   ```

2. Navigate to the directory

   ```
   cd Breast_Cancer_Predictor
   ```

3. Install dependencies

   ```
   pip install -r requirements.txt
   ```

4. Train the model

   ```
   python train_model.py
   ```

5. Run the web application

   ```
   streamlit run web_app.py
   ```

---

## Future Scope

* Integration with healthcare systems (EHR)
* Use of advanced models for improved accuracy
* Deployment as a cloud-based diagnostic tool
* Enhanced visualization and analytics

---

## Conclusion

This project demonstrates how machine learning can be effectively applied to healthcare for early breast cancer detection. It provides a reliable, efficient, and accessible tool that can assist in clinical decision-making while reducing dependency on traditional diagnostic methods.

## Disclaimer

It serves as a supportive diagnostic tool and should not be considered a replacement for expert medical evaluation.