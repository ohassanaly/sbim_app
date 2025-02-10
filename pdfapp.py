import streamlit as st
import PyPDF2
import os

# Set the title of the app
st.title("PDF Text Extractor")

# Create a file uploader for PDF files
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the PDF file
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    
    # Extract text from each page
    for page in reader.pages:
        text += page.extract_text() + '\n'
    
    # Show the extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text from PDF", text, height=300)
    
    # Write the extracted text to a .txt file
    output_file_path = 'output.txt'
    with open(output_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    
    # Provide a download link for the text file
    with open(output_file_path, 'rb') as f:
        st.download_button("Download Text File", f, file_name='output.txt', mime='text/plain')

    # Optionally, you can delete the output file after download
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
