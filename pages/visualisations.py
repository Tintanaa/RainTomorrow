import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

uploaded_file = st.file_uploader("Выберите файл датафрейма", type=["csv", "xlsx", "txt"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file, sep='\t') 

    st.write("Загруженный датафрейм:", df)

    st.title("Датасет Rain in Australia")

st.subheader("ProfileReport")
pr = ProfileReport(df, title="Profile Report")
st_profile_report(pr)

st.header("Зависимость дождя завтра от текущего местоположения в Австралии")
plt.figure(figsize=(15, 10))
sns.countplot(y=df['Location'], hue=df['RainTomorrow'])
st.pyplot(plt)

st.header("Зависимость дождя завтра от минимальной и максимальной температуры")
plt.figure(figsize=(15, 10))
sns.scatterplot(x='MaxTemp', y='MinTemp', data=df, hue='RainTomorrow')
st.pyplot(plt)

st.header("Зависимость дождя завтра от давления и влажности")
fig, axes = plt.subplots(nrows=1, ncols=2)
fig.figsize = (20, 15)
sns.scatterplot(x='Pressure9am', y='Pressure3pm', data=df, hue='RainTomorrow', ax=axes[0])
sns.scatterplot(x='Humidity9am', y='Humidity3pm', data=df, hue='RainTomorrow', ax=axes[1])
st.pyplot(plt)

st.header("Boxplot")
plt.figure(figsize=(40,15))
sns.boxplot(data = df)
st.pyplot(plt)

