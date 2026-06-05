import streamlit as st
import joblib
import pandas as pd

model = joblib.load("flight_price_prediction_model.pkl")

st.title("✈️ Flight Price Predictor")
st.write("Predict Indian domestic flight fares")

airline = st.selectbox("Airline", ['Air Asia', 'Air India', 'GoAir', 'IndiGo',
                                    'Jet Airways', 'Jet Airways Business', 'Multiple carriers',
                                    'Multiple carriers Premium economy', 'SpiceJet', 
                                    'Trujet', 'Vistara', 'Vistara Premium economy'])

source = st.selectbox("Source", ['Banglore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai'])
destination = st.selectbox("Destination", ['Banglore', 'Cochin', 'Delhi', 
                                            'Hyderabad', 'Kolkata', 'New Delhi'])
total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])
journey_day = st.slider("Journey Day", 1, 31, 15)
journey_month = st.slider("Journey Month", 1, 12, 6)
dep_hour = st.slider("Departure Hour", 0, 23, 8)
dep_min = st.slider("Departure Minute", 0, 59, 0)
arrival_hour = st.slider("Arrival Hour", 0, 23, 10)
arrival_min = st.slider("Arrival Minute", 0, 59, 0)
duration_hours = st.slider("Duration (Hours)", 0, 24, 2)
duration_mins = st.slider("Duration (Minutes)", 0, 59, 0)

if st.button("Predict Price"):
    input_dict = {
        'Total_Stops': total_stops,
        'Journey_day': journey_day,
        'Journey_month': journey_month,
        'Dep_hour': dep_hour,
        'Dep_min': dep_min,
        'Arrival_hour': arrival_hour,
        'Arrival_min': arrival_min,
        'Duration_hours': duration_hours,
        'Duration_mins': duration_mins,
    }

    # Airline columns (no prefix, Air Asia is dropped baseline)
    airline_cols = ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
                    'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
                    'Trujet', 'Vistara', 'Vistara Premium economy']
    
    source_cols = ['Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai']
    dest_cols = ['Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
                 'Destination_Kolkata', 'Destination_New Delhi']

    for col in airline_cols + source_cols + dest_cols:
        input_dict[col] = 0

    # Set selected values
    if airline in airline_cols:
        input_dict[airline] = 1  # Air Asia stays all 0s (baseline)
    if f'Source_{source}' in input_dict:
        input_dict[f'Source_{source}'] = 1  # Banglore is baseline (all 0s)
    if f'Destination_{destination}' in input_dict:
        input_dict[f'Destination_{destination}'] = 1  # Banglore is baseline (all 0s)

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Flight Price: ₹{prediction:,.0f}")