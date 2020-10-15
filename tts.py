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
st.sidebar.header("RegClass")
st.sidebar.markdown('<b>Just copy-paste your text here and I will read it out to you</b>', unsafe_allow_html=True)
st.sidebar.markdown('<b>This helps you in meeting your fast approaching deadlines by being highly efficient.</b>', unsafe_allow_html=True)
st.sidebar.markdown('<b>Created by:Nimisha Bhide</b>', unsafe_allow_html=True)
st.sidebar.markdown('<b>Email id:nbhide.nb@gmail.com</b>', unsafe_allow_html=True)
t = st.text_input('Input your sentence here:') 
language="en"
output=gTTS(text=t,lang=language,slow=False)
dt=output.save('output.mp3')
print(dt)
os.system("start output.mp3")
