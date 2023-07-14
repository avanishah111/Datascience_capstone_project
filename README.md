# Car Price Prediction Web App using Streamlit

This repository contains code to build a web application that predicts the selling price of cars based on various features using machine learning.
The model is trained using the Random Forest Regressor algorithm on the car dataset.
## features
Predict the price of a car based on its features.

Explore the dataset and visualize the data.

## Dataset

The dataset used for training the model is available in the file `CAR DETAILS.csv`. 
It contains the following columns:

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

- Python
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
git clone https://github.com/avanishah111/Datascience_capstone_project.git
```
2. Navigate to the project directory.

```bash
cd car-price-prediction-app
```
3. Make sure you have the `CAR DETAILS.csv` file in the project directory.
   
4. Create a virtual environment (optional but recommended) and activate it:
 ```bash
   python -m venv venv
   
For Windows:venv\Scripts\activate

For Unix or Linux:source venv/bin/activate
```
5. Install the required dependencies:
 ```bash 
 pip install -r requirements.txt
 ``` 
6.Run the Streamlit app: 
 ```bash
streamlit run app.py
```
7. Run the Streamlit app.

```bash
streamlit run app.py
```
8. The web app will open in your default browser, and you can use it to predict car prices based on the provided features.

## Model Information

The machine learning model used in this app is based on the Random Forest Regressor algorithm.

The dataset is preprocessed using one-hot encoding for categorical features, and the model is trained on the training set.

The accuracy of the model is evaluated on both the training and testing datasets.

## Contact Or feedback

If you have any questions or feedback, feel free to reach out to the project contributors.

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 
Let's make this project even better together. 

Let's start predicting car prices! Enjoy using the Car Price Prediction model deployed on Streamlit.

Note: This project is for educational purposes only, and the predicted prices should not be considered definitive values for real-world transactions.

## License
This project is licensed under the MIT License.

## References
- Streamlit documentation: [Streamlit](https://docs.streamlit.io/)

---

