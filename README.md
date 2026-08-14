# Car Price Predictor

## Project Overview

Car Price Predictor is a machine learning-based web application that predicts the estimated price of a used car based on selected vehicle attributes.

The project uses Python and Scikit-learn to preprocess the data, train and compare regression models, and select a final model for prediction. The trained model is then integrated into a Streamlit web application.

The predicted price is displayed in Indian Lakhs (₹).

## Objective
* Process a car dataset for machine learning.
* Convert categorical features into numerical values.
* Select relevant features for price prediction.
* Train and compare different regression models.
* Select the best-performing model based on R² score.
* Save the trained model using Pickle.
* Build a Streamlit application for making car price predictions.

## Dataset

The project uses the `Car Dataset Processed.csv` dataset.

The dataset contains information about used cars, including:

* Car name
* Registration year
* Insurance validity
* Fuel type
* Number of seats
* Kilometers driven
* Ownership
* Transmission
* Manufacturing year
* Mileage
* Engine capacity
* Maximum power
* Torque
* Price

The target variable used for prediction is:

`price(in lakhs)`

The dataset contains approximately 1,500 records.

## Data Preprocessing

Categorical variables were converted into numerical values using manually defined mappings.

### Insurance Validity

| Insurance Type        | Encoding |
| --------------------- | -------: |
| Comprehensive         |        5 |
| Third Party insurance |        1 |
| Zero Dep              |        2 |
| Not Available         |        3 |
| Third Party           |        1 |

### Fuel Type

| Fuel Type | Encoding |
| --------- | -------: |
| Petrol    |        0 |
| Diesel    |        1 |
| CNG       |        2 |

### Transmission

| Transmission | Encoding |
| ------------ | -------: |
| Manual       |        5 |
| Automatic    |        1 |

### Ownership

| Ownership    | Encoding |
| ------------ | -------: |
| First Owner  |        1 |
| Second Owner |        2 |
| Third Owner  |        3 |
| Fifth Owner  |        5 |

The registration year was also processed to extract the year component from values such as `Jul-17` and `Jan-21`.

## Features Used

Five features were selected for the final model:

* Insurance Validity
* Fuel Type
* KMs Driven
* Ownership
* Transmission

The target variable is:

* Price in Lakhs

The model development notebook specifically selects these five features for training.

## Machine Learning Models

The project treats car price prediction as a regression problem.

Three regression models were implemented:

### Linear Regression

Used as a baseline regression model.

### K-Nearest Neighbors Regression

A KNN Regressor with 3 neighbors was implemented.

### Support Vector Regression

An SVR model with a polynomial kernel was tested.

## Model Evaluation

The models were compared using the R² score.

| Model                       | R² Score |
| --------------------------- | -------: |
| Linear Regression           |   0.0189 |
| KNN Regressor (3 Neighbors) |   0.5928 |
| Polynomial SVR              |  -0.0022 |

KNN Regressor with 3 neighbors produced the highest score among the three models tested and was selected as the final model.

The final model was saved as `final_model.pkl` using Pickle.

Note: These scores are training R² scores because the models were evaluated on the same data used for training. A separate train/test split or cross-validation would provide a more reliable estimate of the model's performance on unseen data.

## Streamlit Application

The Streamlit application is implemented in `app.py`.

Users can enter the following information:

* Insurance Validity
* Fuel Type
* Ownership
* Transmission Type
* KMs Driven

The application converts the selected categorical values into the numerical representations expected by the trained model.

The inputs are then passed to the saved KNN model to generate a predicted car price.

The result is displayed in Indian Lakhs.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Jupyter Notebook

## Project Structure

```text
Car-Price-Predictor/
│
├── Car Dataset Processed.csv
├── Models.ipynb
├── app.py
├── final_model.pkl
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The project requires:

```text
streamlit
scikit-learn
pandas
numpy
```

## Running the Application

Run the following command from the project directory:

```bash
streamlit run app.py
```

The application will be available at the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

The notebook also documents the use of `streamlit run app.py` to launch the application.

## Author

Rashita Gomes
