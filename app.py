import streamlit as st


options =  ['Vlog no copyright', 'Background music']
st.sidebar.selectbox('Options', options)
st.title('Hello Anumi')
st.write('These are my favourite musics')
days = st.sidebar.slider('Pick your days', min_value=1,max_value=90)
# data_type = st.sidebar.multiselect('Pick data types', data_types)


# video_file = open('Lemon - 82602.mp4')
# video_bytes = video_file.read()

# st.video(video_bytes)

st.video('https://www.youtube.com/watch?v=cGOVqcAzh_8')
