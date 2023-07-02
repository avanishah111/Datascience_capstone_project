# Datascience_capstone_project
To create a readme file that explains the purpose of the project and provides instructions to run the Streamlit app, you can follow the template below:

# Car Price Prediction Web App using Streamlit

This repository contains code to build a web application that predicts the selling price of cars based on various features using machine learning. The model is trained using the Random Forest Regressor algorithm on the car dataset.

## Dataset

The dataset used for training the model is available in the file `CAR DETAILS.csv`. It contains the following columns:

- `name`: Car model name
- `year`: Year of the car
- `selling_price`: Selling price of the car (target variable)
- `km_driven`: Kilometers driven by the car
- `fuel`: Fuel type (Petrol, Diesel, CNG, etc.)
- `seller_type`: Type of seller (Individual, Dealer)
- `transmission`: Transmission type (Manual, Automatic)
- `owner`: Number of previous owners
- `company`: Car manufacturing company

## Prerequisites

To run the Streamlit app, you need to have the following installed on your system:

- Python (version 3.6 or higher)
- pandas
- numpy
- scikit-learn
- streamlit

Install the required dependencies using the following command:

```bash
pip install pandas numpy scikit-learn streamlit
```

## How to Run the Streamlit App

1. Clone this repository to your local machine.

```bash
git clone https://github.com/avanishah111/car-price-prediction-app.git
```

2. Navigate to the project directory.

```bash
cd car-price-prediction-app
```

3. Make sure you have the `CAR DETAILS.csv` file in the project directory.

4. Run the Streamlit app.

```bash
streamlit run app.py
```

5. The web app will open in your default browser, and you can use it to predict car prices based on the provided features.

## Model Information

The machine learning model used in this app is based on the Random Forest Regressor algorithm. The dataset is preprocessed using one-hot encoding for categorical features, and the model is trained on the training set.

The accuracy of the model is evaluated on both the training and testing datasets.

## Contact

If you have any questions or feedback, feel free to reach out to the project contributors.

## References

- Dataset source: [Car Dataset](https://example.com/dataset)
- Streamlit documentation: [Streamlit](https://docs.streamlit.io/)

---

