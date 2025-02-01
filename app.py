# Q&A Chatbot
# from langchain.llms import OpenAI

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

# Add your Gemini API key here directly
GEMINI_API_KEY = "AIzaSyDYzrKkgfYkxNdC3scfqzVQ0scbbXNQja4"

# Configure the Generative AI client with the API key
genai.configure(api_key=GEMINI_API_KEY)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

## Function to load OpenAI model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

## Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    try:
        response = get_gemini_response(input)
        st.subheader("The Response is")
        st.markdown(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
