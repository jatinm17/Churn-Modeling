# Customer Churn Prediction

A web application built with Streamlit to predict customer churn using a pre-trained TensorFlow Keras model.

## Features

- **User-Friendly Interface**: Intuitive UI for easy interaction.
- **Real-Time Predictions**: Instant churn predictions based on user inputs.
- **Tailored Recommendations**: Personalized suggestions to retain customers.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/customer-churn-prediction.git
    cd customer-churn-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure the following files are in the root directory:
    - `model.h5`
    - `label_encoder_gender.pkl`
    - `onehot_encoder_geo.pkl`
    - `scaler.pkl`

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Enter customer details and view the prediction and recommendations.

## Input Features

- Geography, Gender, Age, Credit Score, Balance, Estimated Salary, Tenure, Number of Products, Has Credit Card, Is Active Member.

## Deployment

The application is deployed and accessible at: [Deployment Link](https://jatinm17-churn-modeling-app-5jzdza.streamlit.app/)

## License

This project is licensed under the MIT License.
