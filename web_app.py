import streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Breast Cancer Predictor 🩺")
st.write("AI-powered diagnostic assistant")

# Input fields (30 features simplified)
features = []
feature_names = [
    "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
    "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension",
    "radius error", "texture error", "perimeter error", "area error", "smoothness error",
    "compactness error", "concavity error", "concave points error", "symmetry error", "fractal dimension error",
    "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness",
    "worst compactness", "worst concavity", "worst concave points", "worst symmetry", "worst fractal dimension"
]

st.subheader("Enter Cell Nuclei Features:")

for name in feature_names:
    val = st.number_input(name, value=0.0)
    features.append(val)

features = np.array(features).reshape(1, -1)

# Predict button
if st.button("Predict"):
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0]

    if prediction == 1:
        st.success("✅ Benign (Non-Cancerous)")
    else:
        st.error("⚠️ Malignant (Cancerous)")

    st.write(f"Confidence: {max(prob)*100:.2f}%")

    # Radar Chart (Mean, Error, Worst)
    categories = ["Mean", "Error", "Worst"]

    mean_vals = features[0][:10].mean()
    error_vals = features[0][10:20].mean()
    worst_vals = features[0][20:].mean()

    values = [mean_vals, error_vals, worst_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False
    )

    st.plotly_chart(fig)