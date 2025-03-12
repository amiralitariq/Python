import streamlit as st
import pandas as pd

# App Title
st.title("BMI Calculator")

# Input Sliders
height = st.slider('Enter your height (in cm)', 100, 250, 175)
weight = st.slider('Enter your weight (in kg)', 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Display BMI
st.markdown(f"## Your BMI is: **{bmi:.2f}**")

# Categorizing BMI
if bmi < 18.5:
    category = "Underweight"
    advice = "Consider eating more nutritious food and exercising regularly."
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
    advice = "Great job! Maintain a balanced diet and stay active."
elif 25 <= bmi < 29.9:
    category = "Overweight"
    advice = "Try to incorporate more physical activity and a healthier diet."
else:
    category = "Obese"
    advice = "Consult a healthcare professional for guidance on weight management."

# Display Category & Advice
st.subheader(f"Category: {category}")
st.write(advice)

# BMI Categories Table
st.write("### BMI Categories")
bmi_data = {
    "Category": ["Underweight", "Normal Weight", "Overweight", "Obese"],
    "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30 and above"]
}
df = pd.DataFrame(bmi_data)
st.table(df)

if st.button("Reset"):
    st.rerun()
