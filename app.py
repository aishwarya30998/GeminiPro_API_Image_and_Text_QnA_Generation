# Q&A Chatbot using Gemini pro
from dotenv import load_dotenv

load_dotenv()  # to take environment variables from .env.

import streamlit as st
import os

import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load GeminiPro model and get respones
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')#for text- text input and output
    response = model.generate_content(question)
    return response.text

#initialize our streamlit app
st.set_page_config(page_title=" Q & A Demo")

st.header("Gemini LLM Application for Question and Answering")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

# If submit button is clicked
if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
