import streamlit as st
# Streamlit app UI
st.title("GenAI Text Generator Based on Preceding Input")

# Initialize your generator
generator = pipeline("text-generation", model="gpt2")

input_text = st.text_input("Enter your first words:")
if st.button("Generate"):
    generated_text = generator(input_text, max_length=100, num_return_sequences=1)
    st.write(generated_text[0]['generated_text'])