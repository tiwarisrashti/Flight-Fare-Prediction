# Flight Ticket Price Predictor

![Flight Predictor Logo](flightimg.jpg)

## Overview
This project predicts flight ticket prices based on various features such as airline, source, destination, total stops, and travel date.  
It involves **data preprocessing, exploratory data analysis (EDA), feature engineering, and model training** using regression techniques.

---

## Project Objectives
- Analyze flight fare trends and factors affecting ticket prices.  
- Build a predictive model to estimate flight fares with high accuracy.  
- Deploy a user-interactive app for flight fare prediction (using Streamlit).

---

## Key Features
- Extensive **Exploratory Data Analysis (EDA)** using visualizations.
- **Feature Engineering** for extracting valuable insights (e.g., day, month, duration).
- Model comparison using **Linear Regression and XGBoost**.
- **Optimized model pipeline** saved using `joblib` for future predictions.
- Ready-to-use **Streamlit app** for easy predictions.

---

## Technologies Used
- **Python 3.10+**
- **Libraries:**  
  - pandas, numpy, matplotlib, seaborn  
  - scikit-learn, xgboost  
  - streamlit, joblib  
- **IDE:** Jupyter Notebook / VS Code  
- **Version Control:** Git & GitHub  

---

## Project Structure
flight_project/
│
├── app.py                    # Main Streamlit app script
├── flight_price_pipeline.pkl  # Saved ML model pipeline
├── train_model.ipynb         # Notebook for model training (optional)
├── data/                     # Directory for raw/processed datasets
├── requirements.txt          # Python dependencies
├── flightimg.jpg             # Header image
├── README.md                 # This file

---

## Model Building Steps
1. **Data Loading & Cleaning** – handled missing values, formatted dates.  
2. **Feature Engineering** – derived day, month, duration, and encoded categorical data.  
3. **EDA** – visualized relationships between features and target variable (Price).  
4. **Model Training** – trained and tuned multiple models:
   - Linear Regression   
   - XGBoost Regressor  
5. **Model Evaluation** – evaluated using R², MAE, RMSE.  
6. **Pipeline Creation & Saving** – combined preprocessing and model into one pipeline.

---

## Results
| Model | R² Score | RMSE |
|-------|-----------|------|
| Linear Regression | 0.915 | 6593.23 |
| XGBoost | **0.984** | **2894.52** |

*(Values are indicative and may vary depending on dataset splits.)*

---

## Streamlit App (Optional)
To run the prediction app locally:
```bash
streamlit run app.py
