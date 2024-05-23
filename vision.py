#text and image APP using Gemini Vision Pro
from dotenv import load_dotenv

load_dotenv()  # to take environment variables from .env.

import streamlit as st
import os
from PIL import Image#using python image library to read image and process it to prompt

import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

#initialize our streamlit app

st.set_page_config(page_title="Gemini Vision Pro Image Demo")

st.header("Gemini Vision Pro LLM Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit: 
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
