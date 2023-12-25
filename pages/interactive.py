import streamlit as st
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

st.title("Пытаемся предсказать дождь в Австралии.")

st.header("Выберите район")        
rayon = [2, 4, 10, 11, 21, 24, 26, 27, 30, 34, 37, 38, 42, 45, 47, 9, 40, 23, 5, 6, 35, 19, 18, 20, 25, 33, 44, 12, 7, 8, 14, 39, 0, 22, 28, 48, 1, 46, 29, 32, 31, 36, 43, 15, 17, 3, 13, 16, 41]
rayon.sort()
viborrayona = st.selectbox("Район", rayon, key='rayon')

st.header("Введите минимальную температуру дня")    
mintemp = st.number_input("Значение:", min_value=0.0, max_value=50.0, value=0.0, key='min')

st.header("Введите максимальную температуру дня")    
maxtemp = st.number_input("Значение:", min_value=0.0, max_value=50.0, value=0.0, key='max')

st.header("Введите число осадков сегодня в мм")    
percip = st.number_input("Значение:", min_value=0.0, max_value=1.5, value=0.0, key = 'rainfall')

st.header("Выберите направление порыва ветра")        
windgust = [13, 14, 15, 4, 6, 3, 1, 10, 8, 12, 7, 9, 5, 2, 0, 11]
windgust.sort()
viborwindgust = st.selectbox("Порыв ветра", windgust, key='WindGust')

st.header("Выберите скорость порыва ветра")  
windgustspeed = [44.0, 46.0, 24.0, 41.0, 56.0, 50.0, 35.0, 80.0, 28.0, 30.0, 22.0, 26.0, 43.0, 33.0, 57.0, 48.0, 39.0, 37.0, 52.0, 31.0, 61.0, 54.0, 83.0, 59.0, 70.0, 17.0, 19.0, 63.0, 15.0, 20.0, 13.0, 11.0, 78.0, 74.0, 69.0, 67.0, 76.0, 87.0, 81.0, 65.0, 9.0, 72.0, 85.0, 7.0, 89.0, 91.0, 102.0, 100.0, 113.0, 98.0, 94.0, 107.0, 93.0, 96.0, 104.0, 120.0, 115.0, 109.0, 106.0, 122.0, 124.0, 6.0]
windgustspeed.sort()
viborwindgustspeed = st.selectbox("Скорость порыва ветра", windgustspeed, key='WindGustspeed')

st.header("Выберите месяц наблюдений")  
months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
months.sort()
monthschoose = st.selectbox("Месяц наблюдений", months, key='month')

st.header("Выберите день наблюдений")  
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 12, 13, 14, 15, 18, 19]
days.sort()
days = st.selectbox("Месяц наблюдений", days, key='day')

st.header("Теперь пройдёмся по давлению, влажности, ветру и температуре")

st.subheader("Введите давление, влажность, ветер и температуру в 9 часов утра")
pressure1 = st.number_input("Значение:", min_value=980.0, max_value=1100.0, value=1000.0, key='pressure1')
humidity1 = st.number_input("Значение:", min_value=0.0, max_value=100.0, value=0.0, key='humidity1')
winddir1 = st.number_input("Значение:", min_value=0, max_value=15, value=0, key='wind1')
windspeed1 = st.number_input("Значение:", min_value=0.0, max_value=40.0, value=0.0, key='windspeed1')
temp1 = st.number_input("Значение:", min_value=-10.0, max_value=50.0, value=0.0, key='temp1')

st.subheader("Введите давление, влажность, ветер и температуру в 3 часа вечера")
pressure2 = st.number_input("Значение:", min_value=980.0, max_value=1100.0, value=1000.0, key='pressure2')
humidity2 = st.number_input("Значение:", min_value=0.0, max_value=100.0, value=0.0, key='humidity2')
winddir2 = st.number_input("Значение:", min_value=0, max_value=15, value=0, key='wind2')
windspeed2 = st.number_input("Значение:", min_value=0.0, max_value=40.0, value=0.0, key='windspeed2')
temp2 = st.number_input("Значение:", min_value=-10.0, max_value=50.0, value=0.0, key='temp2')

st.header("По вашему мнению, сегодня был дождь?=) 0 - нет, 1 - да")
choise = st.number_input("Значение:", min_value=0, max_value=1, value=0, key='choise')

data = {'Location': [viborrayona],
        'MinTemp': [mintemp],
        'MaxTemp': [maxtemp], 
        'Rainfall': [percip],
        'WindGustDir': [viborwindgust],
        'WindGustSpeed': [viborwindgustspeed],
        'Month': [monthschoose], 
        'Day': [days],
        'Pressure9am': [pressure1],
        'Humidity9am': [humidity1],
        'Wind9am': [winddir1], 
        'Temperature9am': [temp1],
        'Pressure3pm': [pressure1],
        'Humidity3pm': [humidity1],
        'Wind3pm': [winddir1], 
        'Temperature3pm': [temp1],
        'WindSpeed9am': [windspeed1],
        'WindSpeed3pm': [windspeed2],
        'RainToday': [choise]}
df = pd.DataFrame(data)
X = df.values.flatten()
X = X.reshape(1, -1)

button_clicked = st.button("Предсказать")

if button_clicked:
    st.header("1 - дождь будет")
    st.header("0 - дождя не будет")        
    with open('models/bagging.pkl', 'rb') as file:
            bagging = pickle.load(file)
    import catboost
    
    model = catboost.CatBoostClassifier()
    ctb = model.load_model('models/catboost')
    
    with open('models/SVMbalanced.pkl', 'rb') as file:
            svm_model = pickle.load(file)
    with open('models/xgb.pkl', 'rb') as file:
            pcaxgb = pickle.load(file)
            
    with open('models/stacking.pkl', 'rb') as file:
            stack = pickle.load(file)
    

    model = load_model('models/MLP.keras')
    
    
    st.header("Bagging:")
    st.write(f"{bagging.predict(X)}")
    
    st.header("svm:")
    st.write(f"{svm_model.predict(X)}")
    
    st.header("PCA+XGBoost:")
    st.write(f"{pcaxgb.predict(X)}")


    st.header("NN:")
    prediction = (model.predict(X)>0.5).astype("int32")
    st.write(f"{prediction}")

    st.header("Catboost:")
    st.write(f"{ctb.predict(X)}")
    
    st.header("Stacking:")
    st.write(f"{stack.predict(X)}")


    
    
    

    
