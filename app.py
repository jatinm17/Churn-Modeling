import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Load the encoders and scaler
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1 {
            color: #004d80;
        }
        .stButton button {
            background-color: #004d80;
            color: white;
            border-radius: 5px;
        }
        .stSlider {
            color: #004d80;
        }
        .stNumberInput {
            color: #004d80;
        }
        .stSelectbox {
            color: #004d80;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for additional information or instructions
st.sidebar.title('Customer Churn Prediction')
st.sidebar.write("""
    This application predicts the likelihood of customer churn based on several input features. 
    Please provide the following details to get the churn prediction.
""")

# Main app
st.title('Customer Churn Prediction')

# Layout: Use columns for better alignment
col1, col2 = st.columns(2)

with col1:
    geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
    gender = st.selectbox('Gender', label_encoder_gender.classes_)
    age = st.slider('Age', 18, 92)

with col2:
    credit_score = st.number_input('Credit Score', min_value=0, max_value=1000, value=600)
    balance = st.number_input('Balance', value=0.0)
    estimated_salary = st.number_input('Estimated Salary', value=0.0)

col3, col4 = st.columns(2)

with col3:
    tenure = st.slider('Tenure', 0, 10)
    num_of_products = st.slider('Number of Products', 1, 4)

with col4:
    has_cr_card = st.selectbox('Has Credit Card', [0, 1])
    is_active_member = st.selectbox('Is Active Member', [0, 1])

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

# Display prediction
st.write(f'Churn Probability: {prediction_proba:.2f}')

if prediction_proba > 0.5:
    st.markdown('<h3 style="color: red;">The customer is likely to churn.</h3>', unsafe_allow_html=True)
else:
    st.markdown('<h3 style="color: green;">The customer is not likely to churn.</h3>', unsafe_allow_html=True)
