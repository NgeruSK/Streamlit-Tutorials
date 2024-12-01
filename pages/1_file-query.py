import streamlit as st
import os
import fitz  # PyMuPDF for PDF handling

# Explicitly define the PDF file path in your code
file_path_pdf = "C:/Users/skn2132/Downloads/room-quote.pdf"  # Change to your actual PDF file path

# Streamlit App Title
st.title("PDF File Query App")

# Ensure the PDF file exists
if os.path.exists(file_path_pdf):
    # Extract text from the PDF
    pdf_text = ""
    with fitz.open(file_path_pdf) as doc:
        for page in doc:
            pdf_text += page.get_text()

    # Display the first 500 characters of the PDF content as preview
    st.write("### PDF Content Preview:")
    st.write(pdf_text[:500])  # Show a preview of the first 500 characters

    # Query Section: Allow user to input a search query
    query_value = st.text_input("Enter text to search for in the PDF:")

    if query_value:
        # Search for the query in the PDF text
        matches = [line for line in pdf_text.split("\n") if query_value.lower() in line.lower()]

        if matches:
            st.write(f"### Results for '{query_value}':")
            for match in matches:
                st.write(match)
        else:
            st.write(f"No matches found for '{query_value}' in the PDF.")

    # File Download Section: Allow user to download the extracted content
    if st.button("Download Extracted Content"):
        download_data = pdf_text.encode("utf-8")

        st.download_button(
            label="Download Extracted Content",
            data=download_data,
            file_name="extracted_content.txt",
            mime="text/plain"
        )

else:
    st.warning(f"The PDF file at {file_path_pdf} does not exist.")

# Feedback Section: Allow user to provide feedback
feedback = st.text_area("Provide your feedback on the results")

if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
