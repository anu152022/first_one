import streamlit as st

options =  ['Apple', 'Mango']
st.sidebar.selectbox('Options', options)
st.title('Hello Anumi')
st.write('This is my first web application')

video_file = open('Lemon - 82602.mp4')
video_bytes = video_file.read()

st.video(video_bytes)