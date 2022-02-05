import streamlit as st


options =  ['Vlog no copyright', 'Background music']
st.sidebar.selectbox('Options', options)
st.title('My Covid Dashboard')
st.write('Welcome to my Covid Dashboard')
st.write('Enjoy it well!!')
days = st.sidebar.slider('Pick your number of music', min_value=1,max_value=50)

# video_file = open('Lemon - 82602.mp4')
# video_bytes = video_file.read()

# st.video(video_bytes)

st.video('https://www.youtube.com/watch?v=cGOVqcAzh_8&list=RDcGOVqcAzh_8&start_radio=1')
