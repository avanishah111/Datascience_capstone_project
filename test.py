import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load dataset
df = pd.read_csv('car_newdata.csv')

# Load the pipeline
with open('car_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Create the web app
def main():
    # Set the title and description
    st.title('Car Price Prediction')
    st.write('Enter the details of the car to predict its price.')

    # Get user inputs
    company = st.selectbox('Company Name', sorted(df['company'].unique()))
    name = st.selectbox('Car Name', sorted(df['name'].unique()))
    year = st.number_input('Year', min_value=1900, max_value=2023, step=1)
    km_driven = st.number_input('Kilometers Driven', step=1000)
    fuel = st.selectbox('Fuel Type', df['fuel'].unique())
    seller_type = st.selectbox('Seller Type', df['seller_type'].unique())
    transmission = st.selectbox('Transmission', df['transmission'].unique())
    owner = st.selectbox('Owner', df['owner'].unique())

    data = pd.DataFrame({'company': [company],
                         'name': [name],
                         'year': [year],
                         'km_driven': [km_driven],
                         'fuel': [fuel],
                         'seller_type': [seller_type],
                         'transmission': [transmission],
                         'owner': [owner]})

    if st.button('Predict Price'):
        # Extract the transformer and regressor from the pipeline
        transformer, regressor = pipeline

        # Perform one-hot encoding on categorical columns
        data_encoded = transformer.transform(data).toarray()

        # Make predictions
        predictions = regressor.predict(data_encoded)
        st.success(f'Price of the car is {predictions[0]} INR')

# Run the web app
if __name__ == '__main__':
    main()
