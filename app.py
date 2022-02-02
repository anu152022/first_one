import streamlit as st


options =  ['Vlog no copyright', 'Background music']
st.sidebar.selectbox('Options', options)
st.title('My Covid Dashboard')
st.write('Welcome to my Covid Dashboard')
st.write('Enjoy it well!!')
days = st.sidebar.slider('Pick your number of music', min_value=1,max_value=90)

# video_file = open('Lemon - 82602.mp4')
# video_bytes = video_file.read()

# st.video(video_bytes)

page_bg_img = '''
<style>
body {
background-image: url("https://media.istockphoto.com/photos/blue-picture-id1213090148?k=20&m=1213090148&s=170667a&w=0&h=OheD3nObHHYhgIQw30xo-m1mDseWmkshgPiM-sgNgjE=");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
