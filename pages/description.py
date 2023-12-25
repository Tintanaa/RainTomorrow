import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="description")

st.write("# Описание ")

st.markdown(
    """
    
    Для выполнения РГР мною был выбран датафрейм для классификации Rain in Australia
    
    Задача: бинарная классификация - предсказание RainTomorrow таргета 
    
    (будет ли дождь в Австралии завтра?).
    
    Ссылка: https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
    
    ### В приложении представлено 6 моделей:
    
    - SVM (классическая модель обучения с учителем)
    
    - PCA + XGboost /-/ 
    
    - catboost (ансамблевая модель (градиентный бустинг))
    
    - bagging (ансамблевая модель (бэггинг))
    
    - stacking (ансамблевая модель (стэкинг)) 
    
    - Глубокая полносвязная нейронная сеть на Keras
   
    
    При сериализации моделей использовал модуль pickle а также встроенные инструменты в случае catboost, MLP, XGBoost
    
    ### Все модели обучены и протестированы на 111197 наблюдениях (80% тренировочная выборка, 20% тестовая)

    ## Количество признаков: 19
    ### Названия:
    - Location,
    - MinTemp,
    - MaxTemp,
    - Rainfall,
    - WindGustDir,
    - WindGustSpeed,
    - WindDir9am,
    - WindDir3pm,
    - WindSpeed9am,
    - WindSpeed3pm,
    - Humidity9am,
    - Humidity3pm,
    - Pressure9am,
    - Pressure3pm,
    - Temp9am,
    - Temp3pm,
    - RainToday,
    - month,
    - day

    ## Таргет: 1
    Название:     
    - RainTomorrow

    ### Отбор признаков производился после проведения EDA над изначальным датафреймом:
    
    1) ydata_profiling (вывод всей информации о датасете и характере данных внутри него)
    
    2) Построение графиков интересующих величин для определения их характера и вида распределения.
    
    3) Предобработка (удаление ненужных признаков/ заполнение нулевых строк... )
    
    4) Выявление наиболее значимых признаков используя в связке показатели gini и p-value.

    """, unsafe_allow_html=True
)

st.markdown(
    """
    ### Оценка качества NN
    """
    , unsafe_allow_html=True
)

st.image('assets/png/MLP.png')

st.markdown(
    """
    ### Оценка качества bagging
    """
    , unsafe_allow_html=True
)

st.image('assets/png/bagging.png')

st.markdown(
    """
    ### Оценка качества catboost
    """
    , unsafe_allow_html=True
)

st.image('assets/png/catboost.png')

st.markdown(
    """
    ### Оценка качества SVM
    """
    , unsafe_allow_html=True
)

st.image('assets/png/SVM.png')

st.markdown(
    """
    ### Оценка качества PCA + XGBoost
    """
    , unsafe_allow_html=True
)

st.image('assets/png/PCA+XGBoost.png')

st.markdown(
    """
    ### Оценка качества Stacking
    """
    , unsafe_allow_html=True
)

st.image('assets/png/stacking.png')