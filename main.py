import streamlit as st

st.set_page_config(
    page_title="RGR Myagkov FIT-222",
)

st.write("<h1 style='text-align: center; color: white;'>Главная</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <p style="text-align: center;"> Привет! Меня зовут Мягков Егор, я из группы ФИТ-222 </p>
    <p style="text-align: center;"> (Just another one photo). </p>
    """, unsafe_allow_html=True
)

st.image('assets/png/1703511503836.jpg')

st.markdown(
    """
    <p style="text-align: center;"> (LOGO). </p>
    """, unsafe_allow_html=True
)

title_vid = open('assets/vids/0000-0377.mp4', 'rb')
video1 = title_vid.read()
st.video(video1)

st.markdown(
    """
    <p style="text-align: center;">
        <span style="color: #ffffff; font-family: Neotriad; font-size: 24pt;">Machine learning routine</span>
    </p>
    
    Это проект созданный для РГР по машинному обучению
    
    В нём я показал свои знания полученные в области ML за 3 семестр обучения в ОМГТУ
    
    Но это не значит, что он не будет обновляться...
    
    Основные использованные технологии: 
    - sklearn, 
    - tensorflow, 
    - streamlit
    
    <p style="text-align: center;"> Данный проект содержит в себе 6 моделей машинного обучения для предсказания дождя в Австралии на завтрашний день</p>
    
    <p style="text-align: center;"> За дальнейшими подробностями смотреть в description </p>
    """, unsafe_allow_html=True
    )