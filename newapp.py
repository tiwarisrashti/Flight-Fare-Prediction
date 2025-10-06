import streamlit as st
import pandas as pd
import joblib

# Load the saved pipeline
pipeline = joblib.load("flight_price_pipeline.pkl")

st.set_page_config(page_title="Flight Price Predictor", layout="centered")
st.image("flightimg.jpg", use_container_width=True)
st.title("Flight Ticket Price Predictor")
st.markdown("Predict approximate ticket price based on flight details")

# Create three columns for input fields
col1, col2, col3 = st.columns(3)

# First column: Airline, Source City, Destination City
with col1:
    airline = st.selectbox("Airline", ["SpiceJet","IndiGo","Air India","Vistara","GoAir"])
    source_city = st.selectbox("Source City", ["Delhi","Mumbai","Bangalore","Kolkata","Chennai"])
    destination_city = st.selectbox("Destination City", ["Delhi","Mumbai","Bangalore","Kolkata","Chennai"])

# Second column: Departure Time, Arrival Time, Stops
with col2:
    departure_time = st.selectbox("Departure Time", ["Early_Morning","Morning","Afternoon","Evening","Night"])
    arrival_time = st.selectbox("Arrival Time", ["Morning","Afternoon","Evening","Night"])
    stops = st.selectbox("Stops", ["zero","one","two_or_more"])

# Third column: Days Left, Class, Duration
with col3:
    days_left = st.slider("Days Left Before Departure", 0, 365, 10)
    flight_class = st.radio("Class", ["Economy","Business"])
    duration = st.number_input("Duration (hours)", min_value=0.5, max_value=20.0, value=2.0, step=0.25)

# Feature engineering
route = f"{source_city}_{destination_city}"
is_peak_time = 1 if departure_time in ["Morning","Evening"] else 0
is_red_eye = 1 if departure_time == "Night" else 0

# Duration category
if duration <= 2:
    duration_category = 'short'
elif duration <= 4:
    duration_category = 'medium'
else:
    duration_category = 'long'

# Days left bucket
if days_left == 0:
    days_left_bucket = '0'
elif days_left <= 3:
    days_left_bucket = '1-3'
elif days_left <= 7:
    days_left_bucket = '4-7'
elif days_left <= 14:
    days_left_bucket = '8-14'
elif days_left <= 30:
    days_left_bucket = '15-30'
elif days_left <= 60:
    days_left_bucket = '31-60'
else:
    days_left_bucket = '61+'

# Prepare input dataframe
input_df = pd.DataFrame([{
    'airline': airline,
    'source_city': source_city,
    'destination_city': destination_city,
    'departure_time': departure_time,
    'arrival_time': arrival_time,
    'stops': int(0 if stops=='zero' else (1 if stops=='one' else 2)),
    'class': flight_class,
    'duration': float(duration),
    'days_left': int(days_left),
    'route': route,
    'is_peak_time': is_peak_time,
    'is_red_eye': is_red_eye,
    'duration_category': duration_category,
    'days_left_bucket': days_left_bucket
}])

# Hide the input dataframe
# (No st.table(input_df.T) line included)

if st.button("Predict Price"):
    pred = pipeline.predict(input_df)[0]
    st.success(f"Estimated Ticket Price: ₹{int(pred)}")
    st.info("Model prediction is approximate — use for guidance only.")