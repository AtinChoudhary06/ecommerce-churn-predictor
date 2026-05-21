import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")

# Title
st.title("E-Commerce Customer Churn Prediction")

st.write("Enter customer details below")

# =========================
# USER INPUTS
# =========================

age = st.number_input("Age", min_value=18, max_value=100)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

city = st.selectbox(
    "City",
    ["Delhi", "Mumbai", "Bangalore", "Chennai"]
)

tenure_months = st.number_input("Tenure Months", min_value=0)

avg_order_value = st.number_input("Average Order Value", min_value=0.0)

total_orders = st.number_input("Total Orders", min_value=0)

last_purchase_days_ago = st.number_input(
    "Last Purchase Days Ago",
    min_value=0
)

support_tickets = st.number_input(
    "Support Tickets",
    min_value=0
)

subscription_type = st.selectbox(
    "Subscription Type",
    ["Basic", "Standard", "Premium"]
)

# =========================
# ENCODING
# =========================

# Gender Encoding
gender = 1 if gender == "Male" else 0

# City Encoding
city_mapping = {
    "Delhi": 0,
    "Mumbai": 1,
    "Bangalore": 2,
    "Chennai": 3
}

city = city_mapping[city]

# Subscription Encoding
subscription_mapping = {
    "Basic": 0,
    "Standard": 1,
    "Premium": 2
}

subscription_type = subscription_mapping[subscription_type]

# =========================
# PREDICTION
# =========================

if st.button("Predict"):

    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'city': [city],
        'tenure_months': [tenure_months],
        'avg_order_value': [avg_order_value],
        'total_orders': [total_orders],
        'last_purchase_days_ago': [last_purchase_days_ago],
        'support_tickets': [support_tickets],
        'subscription_type': [subscription_type]
    })

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)[0][1]

    st.write(f"Churn Probability: {probability:.2f}")

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Stay")