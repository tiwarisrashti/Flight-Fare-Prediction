# Flight Ticket Price Predictor

![Flight Predictor Logo](flightimg.jpg)

This repository contains an end-to-end Machine Learning project for predicting flight ticket prices using the XGBoost algorithm and a Streamlit-based web interface. The project leverages historical flight data to forecast approximate ticket prices based on various features such as airline, source and destination cities, departure/arrival times, stops, class, duration, and days left before departure.
The model is trained on a dataset typically sourced from platforms like Kaggle (e.g., flight price prediction datasets), involving extensive data preprocessing, feature engineering, model training, and evaluation. The Streamlit app provides a user-friendly interface for real-time predictions.

## Features

- Data Preprocessing: Handling missing values, encoding categorical variables (e.g., airlines, cities), and parsing date-time information.
- Feature Engineering: Creating derived features like route (source_destination), peak time indicators, red-eye flights, duration categories (short/medium/long), and days-left buckets (e.g., 1-3, 4-7, 8-14).
- Model Training: Utilizes XGBoost regressor for accurate price prediction, with hyperparameter tuning for optimal performance (e.g., R² score around 0.5 or higher on test data).
- Evaluation: Metrics such as Mean Squared Error (MSE), R² score, and cross-validation to assess model accuracy.
- Deployment: Interactive web app built with Streamlit for inputting flight details and displaying predictions. The app includes an image header, columnar layout for inputs, and hides internal dataframes for a clean UI.

The app predicts prices in Indian Rupees (₹) and includes a disclaimer that predictions are approximate.

## Model Performance

Test RMSE: 2894.52
Test MAE: 1568.76
Test R²: 0.984
These metrics indicate a highly accurate model, with an R² of 0.984 suggesting that 98.4% of the variance in ticket prices is explained by the model.

## Project Structure

Flight-Fare-Prediction/
│
├── app.py              # Main Streamlit app script
├── flight_price_pipeline.pkl  # Saved ML model pipeline
├── train_model.ipynb   # Notebook for model training (optional)
├── data/               # Directory for raw/processed datasets
├── requirements.txt    # Python dependencies
├── flightimg.jpg       # Header image
├── README.md           # This file