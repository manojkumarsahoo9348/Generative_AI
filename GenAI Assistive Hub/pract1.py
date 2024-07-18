import streamlit as st
from PIL import Image
import google.generativeai as genai

# Function to initialize GenAI with API key (replace 'YOUR_API_KEY' with your actual API key)
def initialize_genai():
    api_key = 'AIzaSyC9XAtwoCOdayscdFrXxKXBELiKcTYBhzo'  # Replace with your actual API key
    genai.configure(api_key=api_key)

# Function to process the image and generate text using GenAI
def process_and_generate_image_text(image_file):
    try:
        img = Image.open(image_file)
        model = genai.GenerativeModel('gemini-1.5-flash')  # Adjust model name based on GenAI capabilities
        response = model.generate_content(img)
        return response.text, img
    except Exception as e:
        st.error(f"An error occurred processing the image: {e}")
        return None, None

# Function to generate text using GenAI based on user input
def process_and_generate_text_to_text(user_input):
    try:
        model = genai.GenerativeModel('gemini-pro')  # Adjust model name based on GenAI capabilities
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        st.error(f"An error occurred generating text: {e}")
        return None

# Main function for Streamlit app
def main():
    st.markdown("<h1 style='color: red;'>I AM YOUR PERSONAL AI ❤</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #0089FF;'>💙 I provide answers to any questions you may have and generate descriptive text from images you upload.</h2>", unsafe_allow_html=True)
    
    initialize_genai()  # Initialize GenAI with your API key

    # Text input section
    user_input = st.text_input("Enter your doubt", key="user_input")
    submit_button = st.button("SUBMIT")

    if submit_button and user_input:
        generated_text = process_and_generate_text_to_text(user_input)
        if generated_text:
            st.success("Read below:")
            st.write(generated_text)
        else:
            st.warning("Text generation failed. Please try again.")

    # Image upload section
    uploaded_file = st.file_uploader("Upload an image (JPEG or PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        generated_text, processed_image = process_and_generate_image_text(uploaded_file)
        if generated_text:
            st.success("Image Description:")
            st.write(generated_text)

            # Display the uploaded image
            st.subheader("Uploaded Image")
            col1, col2 = st.columns(2)
            with col1:
                st.image(processed_image, use_column_width=True)

if __name__ == '__main__':
    main()
