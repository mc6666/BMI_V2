# 執行：streamlit run HW3_BMI_計算器網頁_Solution.py

import streamlit as st

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('./style.css')

st.title('BMI值計算器')

h = st.slider('身高(公分):', 100, 200, 170, 5)
w = st.slider('體重(公斤):', 30, 150, 50, 5)
gender = st.radio('性別:', ('女性', '男性'))
Waistline = st.number_input('腰圍(英吋):', 20, 50, 30)

if st.button('計算'):
    h1 = float(h) / 100
    w = float(w)

    BMI = w / (h1 ** 2)
    BMI = round(BMI, 2)
    message = f'BMI={BMI}, '
    if BMI < 18.5:
        message += '太輕'
    elif BMI < 25:
        message += '正常'
    elif BMI < 30:
        message += '過重'
    else:
        message += '肥胖'

    message += ', '
        
    if gender == '女性' and 2.54 * Waistline >= 80.0:
        message += '腰圍異常'
    elif gender == '男性' and 2.54 * Waistline >= 90.0:
        message += '腰圍異常'
    else:
        message += '腰圍正常'

    st.text("")
    st.write(message)   

            
    