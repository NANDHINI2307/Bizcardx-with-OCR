import streamlit as st
import easyocr
import io
from PIL import Image
import numpy as np
import mysql.connector
import re

# Establish a MySQL connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="white",
    database="ocr_reader"
)

def create_table():
    # Create the 'business_cards' table if it doesn't exist
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS business_cards (
            id INT AUTO_INCREMENT PRIMARY KEY,
            card_holder_name VARCHAR(255),
            designation VARCHAR(255),
            mobile_number1 VARCHAR(200),
            email_address VARCHAR(255),
            website_url VARCHAR(255),
            address VARCHAR(255)
        )
    """)
    db_connection.commit()

def insert_data(data):
    # Convert the list of mobile numbers to a string
    mobile_numbers = ', '.join(data[2])

    # Insert the extracted data into the 'business_cards' table
    cursor = db_connection.cursor()
    query = """
        INSERT INTO business_cards
        (card_holder_name, designation, mobile_number1, email_address, website_url, address)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (data[0], data[1], mobile_numbers, data[3], data[4], data[5])
    
    cursor.execute(query, values)
    db_connection.commit()

def extract_information(image):
    try:
        reader = easyocr.Reader(["en"])
        results = reader.readtext(image)

        # Extracted information from the results
        card_holder_name = ""
        designation = ""
        mobile_numbers = []
        email_address = ""
        website_url = ""
        address_lines = []

        # Define patterns for mobile numbers, email address, and website URL
        mobile_pattern = re.compile(r'\+\d{1,3}-\d{3}-\d{3,}')
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        website_pattern = re.compile(r'(www\.)?[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}')

        # Assume the first result is the card holder's name and the second is the designation
        if results:
            card_holder_name = results[0][1].strip()
        if len(results) > 1:
            designation = results[1][1].strip()

        # Extract mobile numbers, email address, website URL, and address
        for result in results[2:]:
            text = result[1]

            if mobile_pattern.search(text):
                mobile_numbers.append(mobile_pattern.search(text).group())
            elif email_pattern.search(text):
                email_address = email_pattern.search(text).group()
            elif website_pattern.search(text):
                website_url = website_pattern.search(text).group()
            else:
                address_lines.append(text.strip())

        address = ', '.join(address_lines)

        return card_holder_name, designation, mobile_numbers, email_address, website_url, address
    except Exception as e:
        st.error(f"Error during OCR: {str(e)}")
        return None

def display_results(card_holder_name, designation, mobile_numbers, email_address, website_url, address):
    st.write(f"Card Holder Name: {card_holder_name}")
    st.write(f"Designation: {designation}")
    st.write(f"Mobile Numbers: {', '.join(mobile_numbers)}")
    st.write(f"Email Address: {email_address}")
    st.write(f"Website URL: {website_url}")
    st.write(f"Address: {address.replace(' ;', ',')}")

# Create the Streamlit application layout
st.title("BizCardX: Extracting Business Card Data with OCR")

# Add a file uploader to allow users to upload the business card image
image = st.file_uploader("Upload Business Card Image", type=["jpg", "jpeg", "png"])

# Check if the user has uploaded a business card image
if image is not None:
    # Extract the information from the image
    image_pil = Image.open(image)
    image_array = np.array(image_pil)
    create_table()
    extracted_data = extract_information(image_array)

    if extracted_data is not None:
        # Insert the extracted data into the MySQL database
        insert_data(extracted_data)

        # Display the extracted information
        display_results(*extracted_data)

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)
else:
    # Handle the case where the user has not uploaded a business card image yet
    # For example, you can display a message to the user
    st.info("Please upload a business card image.")
