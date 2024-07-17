import streamlit as st
import pathlib
import textwrap

from PIL import Image

import os
# Configure API key
os.environ['GEMINI_API_KEY'] = 'AIzaSyD-zTeXFgWMFPvEndsCP-RGuSv-P1DuNYE'

import google.generativeai as genai

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Function to get Gemini response
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-pro-vision')

    if input_text != "":  # Fixed the equality check here
        response = model.generate_content([image])
    else:
        response = model.generate_content([input_text, image])
    
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title='IMAGE CREATION')
st.header('GEMINI AI IMAGE APP ANALYSIS')

input_text = st.text_input('Input Prompt', key='input')

upload_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit = st.button('Explain Brief About image')

if submit:
    if image:
        response = get_gemini_response(input_text, image)
        st.subheader('The response is:')
        st.write(response)
    else:
        st.error("Please upload an image.")
