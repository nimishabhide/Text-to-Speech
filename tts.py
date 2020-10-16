import streamlit as st
from gtts import gTTS
import os
st.set_option('deprecation.showfileUploaderEncoding', False)

html_temp = """
    <div style="background-color:black ;padding:10px">
    <h1 style="color:white;text-align:center;">TALK WITH ME</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
html_temp69 = """
    <div style="background-color:white ;padding:10px">
    <h3 style="color:black;text-align:center;">PLEASE HAVE A LOOK AT THE SIDEBAR TO MAKE THE BEST USE OF this WEBAPP</h3>
    </div>
    """
st.markdown(html_temp69, unsafe_allow_html=True)
st.sidebar.header("Your friend who will take the place of your grandma and read out stories to you")
st.sidebar.markdown('<b>Just copy-paste your text here and I will read it out to you</b>', unsafe_allow_html=True)
st.sidebar.markdown('<b>This helps you in meeting your fast approaching deadlines by being highly efficient.</b>', unsafe_allow_html=True)
st.sidebar.markdown('<b>Created by:Nimisha Bhide</b>', unsafe_allow_html=True)
st.sidebar.markdown('<b>Email id:nbhide.nb@gmail.com</b>', unsafe_allow_html=True)
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    df = extract_data(uploaded_file)
    fh=open(df,"r")
    myText=fh.read()
language="en"
output=gTTS(text=myText,lang=language,slow=False)
output.save("voice.ogg")
audio_file = open('voice.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')
