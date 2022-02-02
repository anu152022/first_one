import streamlit as st

options =  ['Vlog no copyright', 'Background music']
st.sidebar.selectbox('Options', options)
st.title('Hello Anumi')
st.write('These are my favourite musics')


# video_file = open('Lemon - 82602.mp4')
# video_bytes = video_file.read()

# st.video(video_bytes)

st.video('https://www.youtube.com/watch?v=cGOVqcAzh_8')
