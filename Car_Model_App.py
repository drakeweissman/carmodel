import xgboost as xgb
import streamlit as st
import pandas as pd

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

#Caching the model for faster loading
@st.cache

#Setup inputs to prediction function
#Logic to turn those 6 into 17 columns
def predict(category, manu,fueltype, mileage, geartype, airbags, cylinders):
    Mileage = mileage
    Airbags = airbags

    cat_Sedan = 0
    cat_Jeep = 0
    cat_Hatchback = 0
    if category == 'Sedan':
        cat_Sedan = 1
    elif category == 'SUV':
        cat_Jeep = 1
    elif category == 'Hatchback':
        cat_Hatchback = 1

    fuel_Petrol = 0
    fuel_Diesel = 0
    if fueltype == 'Petrol':
        fuel_Petrol = 1
    elif fueltype == 'Diesel':
        fuel_Diesel = 1

    cyl_6 = 0
    cyl_8 = 0
    if cylinders == 6:
        cyl_6 = 1
    elif cylinders == 8:
        cyl_8 = 1

    manu_HYUNDAI = 0
    manu_TOYOTA = 0
    manu_MERCEDES = 0
    manu_FORD = 0
    manu_BMW = 0
    manu_LEXUS = 0
    manu_HONDA = 0
    if manu == 'Hyundai':
        manu_HYUNDAI = 1
    elif manu == 'Toyota':
        manu_TOYOTA = 1
    elif manu == 'Mercedes':
        manu_MERCEDES = 1  
    elif manu == 'Ford':
        manu_FORD = 1
    elif manu == 'BMW':
        manu_BMW = 1
    elif manu == 'Lexu':
        manu_LEXUS = 1
    elif manu == 'Honda':
        manu_HONDA = 1

    if geartype == 'Automatic':
        gear_Automatic = 1
    else:
        gear_Automatic = 0

    prediction = model.predict(pd.DataFrame([[Mileage, Airbags, cat_Sedan, cat_Jeep, cat_Hatchback, fuel_Petrol, fuel_Diesel,cyl_6, cyl_8, manu_HYUNDAI, manu_TOYOTA, manu_MERCEDES, manu_FORD, manu_BMW, manu_LEXUS, manu_HONDA, gear_Automatic]], 
    columns=['Mileage', 'Airbags', 'cat_Sedan', 'cat_Jeep', 'cat_Hatchback','fuel_Petrol', 'fuel_Diesel', 'cyl_6', 'cyl_8', 'manu_HYUNDAI','manu_TOYOTA', 'manu_MERCEDES-BENZ', 'manu_FORD', 'manu_BMW','manu_LEXUS', 'manu_HONDA', 'gear_Automatic']))
    return prediction


#Create app design
st.title('Car Price Predictor')
st.image("""https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2019-honda-civic-sedan-1558453497.jpg?crop=1xw:0.9997727789138833xh;center,top&resize=480:*""")
st.header('Enter the characteristics of the car:')

#Define user inputs. Need to determine min and max. Type of input
manu = st.selectbox('Manufacturer:', ['Toyota', 'Hyundai', 'Ford', 'Mercedes', 'BMW', 'Honda', 'Lexus', 'Volkswagen','Nisaan', 'Chevrolet','Jeep','Tesla','Land Rover'])
category = st.selectbox('Category:', ['Sedan', 'SUV', 'Hatchback'])
make = st.text_input('Make:', placeholder='Corolla')
mileage = st.slider('Mileage (km):', 0,500000, 150000, step = 1000)
fueltype = st.selectbox('Fuel Type:', ['Petrol', 'Diesel', 'Hybrid', 'Other'])
geartype = st.selectbox('Gear Box Type:', ['Automatic', 'Tiptronic', 'Manual', 'Variator'])
cylinders = st.slider('Number of Cylinders:', 4,8, 4, step = 2)
airbags = st.slider('Number of Airbags:', 0,12,10, step = 2)


#Make prediction when button is clicked
if st.button('Predict Price'):
    price = predict(category, manu,fueltype, mileage, geartype, airbags, cylinders)
    st.success(f'The predicted price of the car is ${price[0]:.2f} USD')
