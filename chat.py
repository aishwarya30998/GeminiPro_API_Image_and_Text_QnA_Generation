#  Q and A chat using Gemini PRO as it stores history for context based answering
from dotenv import load_dotenv

load_dotenv()  # to take environment variables from .env.

import streamlit as st
import os

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

#initialize streamlit app

st.set_page_config(page_title="Q&A incontext chat history Demo")

st.header("Gemini Pro LLM Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)
