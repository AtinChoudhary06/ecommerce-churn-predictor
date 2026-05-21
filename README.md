# 🛒 E-Commerce Customer Churn Prediction

A machine learning web application that predicts whether an e-commerce customer is likely to churn, built with Python, Scikit-learn, and Streamlit — deployed on Render.

## 🔗 Live Demo
👉 [Click here to view the app](#) <!-- Replace with your Render URL -->

---

## 📌 Overview

Customer churn is one of the biggest challenges for e-commerce businesses. This app allows businesses to input customer details and instantly predict the probability of churn using a trained machine learning model.

---

## 🚀 Features

- Predicts customer churn in real time
- Clean and simple UI built with Streamlit
- Trained ML model using Scikit-learn
- Deployed publicly on Render

---

## 🧠 Machine Learning

- **Algorithm:** Random Forest Classifier (or update with your actual model)
- **Dataset:** E-commerce customer churn dataset with 10,000+ records
- **Input Features:**
  - Age
  - Gender
  - City
  - Tenure Months
  - Average Order Value
  - Total Orders
  - Last Purchase Days Ago
  - Support Tickets
  - Subscription Type

- **Output:** Churn / No Churn + Probability Score

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Scikit-learn | ML model training |
| Pandas | Data handling |
| Joblib | Model serialization |
| Render | Deployment |

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── app.py                  # Streamlit web app
├── churn_model.pkl         # Trained ML model
├── requirements.txt        # Python dependencies
├── EDA.ipynb               # Exploratory Data Analysis notebook
└── README.md               # Project documentation
```

---

## ⚙️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 📊 EDA Highlights

Exploratory Data Analysis was performed on the dataset covering:
- Churn rate distribution
- Feature correlations
- Customer segmentation by subscription type and city

See `EDA.ipynb` for full analysis.

---

## 🙋‍♂️ Author

**Atin Choudhary**  
📧 atin06choudhary@gmail.com  
🔗 [GitHub](https://github.com/AtinChoudhary06)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
