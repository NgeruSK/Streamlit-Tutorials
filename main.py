import streamlit as st
from transformers import pipeline

# Initialize your generator
generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")
# generator = pipeline("text-generation")


st.title("GenAI Code Completion")
prompt = st.text_input("What is your first code snip like?")

if(st.button("Generate")):
    # Complete code snippet
    completed_code = generator(prompt, max_length=250, num_return_sequences=1)

    st.text(completed_code[0]['generated_text'])

