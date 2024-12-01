import streamlit as st
import fitz  # PyMuPDF for PDF handling
import re  # Regular expression for pattern matching

# Streamlit App Title
st.title("PDF File Query App - Dynamic Search")

# File Upload Section
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    pdf_text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            pdf_text += page.get_text()

    # Display the first 500 characters of the PDF content as a preview
    st.write("### PDF Content Preview:")
    st.write(pdf_text[:500])  # Show a preview of the first 500 characters

    # Query Section: Allow the user to input any search query
    query_value = st.text_input("Enter your search query:")

    if query_value:
        # Search for the query in the PDF text
        pattern = re.compile(re.escape(query_value), re.IGNORECASE)  # Case-insensitive search
        matches = pattern.findall(pdf_text)

        # Highlight matching lines containing the query
        lines_with_matches = [
            line for line in pdf_text.split('\n') if query_value.lower() in line.lower()
        ]

        if matches:
            st.write(f"### Found {len(matches)} occurrence(s) of '{query_value}':")
            for line in lines_with_matches:
                st.write(f"- {line}")
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
    st.info("Please upload a PDF file to start querying.")

# Feedback Section: Allow user to provide feedback
feedback = st.text_area("Provide your feedback on the results")

if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
