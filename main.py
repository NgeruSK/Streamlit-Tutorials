import streamlit as st
from transformers import pipeline

# Initialize your generator
generator = pipeline("text-generation", model="gpt2")


st.title("GenAI Intro Preview")
fav_meal = st.text_input("What is your favourite meal?")

st.text(f"Input favourite meal is: {fav_meal}")

