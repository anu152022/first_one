import streamlit as st


options =  ['Vlog no copyright', 'Background music']
st.sidebar.selectbox('Options', options)
st.title('My Covid Dashboard')
st.write('Welcome to my Covid Dashboard')
st.write('Enjoy it well!!')
days = st.sidebar.slider('Pick your number of music', min_value=1,max_value=90)

video_file = open('Lemon - 82602.mp4')
video_bytes = video_file.read()

st.video(video_bytes)

page_bg_img = '''
<style>
body {
background-image: url("https://media.istockphoto.com/photos/coronavirus-virus-outbreak-picture-id1206774789?k=20&m=1206774789&s=612x612&w=0&h=7MgIbLQbVUCSic3wnpcqAj-0fNZdD_s-w5QTVxO_MNU=");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
