from sklearn.model_selection import train_test_split
import pandas as pd
from xgboost.sklearn import XGBRegressor
df = pd.read_csv('car_price_prediction.csv')
df = df.drop_duplicates()
df = df.drop(columns = ['Levy','Wheel','ID','Color','Engine volume', 'Model', 'Leather interior','Prod. year','Doors', 'Drive wheels'])
cat_dummies = pd.get_dummies(df.Category, prefix='cat')[['cat_Sedan', 'cat_Jeep','cat_Hatchback']]
df = pd.concat([df, cat_dummies], axis = 1)
fuel_dummies = pd.get_dummies(df['Fuel type'], prefix='fuel')[['fuel_Petrol','fuel_Diesel']]
df = pd.concat([df, fuel_dummies], axis = 1)
df["Mileage"] = df["Mileage"].str[:-3].astype(int)
df['Cylinders'] = df['Cylinders'].astype(int)
cyl_dummies = pd.get_dummies(df['Cylinders'], prefix='cyl')[['cyl_6','cyl_8']]
df = pd.concat([df, cyl_dummies], axis = 1)
manu_dummies = pd.get_dummies(df['Manufacturer'], prefix='manu')[['manu_HYUNDAI','manu_TOYOTA','manu_MERCEDES-BENZ','manu_FORD','manu_BMW','manu_LEXUS','manu_HONDA']]
df = pd.concat([df, manu_dummies], axis = 1)
gear_dummies = pd.get_dummies(df['Gear box type'], prefix='gear')['gear_Automatic']
df = pd.concat([df, gear_dummies], axis = 1)
df = df.drop(columns = ['Category', 'Fuel type','Cylinders','Manufacturer','Gear box type'])
y = df['Price']
X = df.drop(columns='Price')
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state = 1)
xgb = XGBRegressor()
xgb.fit(X_train,y_train)
xgb.save_model('xgb_model.json')