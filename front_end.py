import streamlit as st
import numpy as np
import pandas as pd


## Title
st.title("Streamlit Tutorial")
## Header/Subheader
st.header("This is header")
st.subheader("This is subheader")
## Text
st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")
        
st.write('# 마크다운 된(#) View의 타이틀')
st.write('## raw')
view = [100, 150, 30]
st.write('## bar chart')
st.bar_chart(view)
sview = pd.Series(view)  #pandas 로 읽을 수 있음
sview

st.markdown("""Markdown""")

st.checkbox("please check me")

df = pd.DataFrame({
    'first column': list(range(1,11)),
    'second column': np.arange(10, 101, 10)
})

line_count = st.slider('Select a line count', 1, 10, 3)

head_df = df.head(line_count)

head_df


