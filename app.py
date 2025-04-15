
import streamlit as st

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb+srv://prabhatdsc487:prabha123@app-cluster.9joou.mongodb.net/?retryWrites=true&w=majority&appName=app-cluster"
# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))
db=client['cricket']
collection=db['match_poll']
   

def main():
    st.title("🔐 User Registration Form")

    # Collect user input
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    dob = st.date_input("Date of Birth")
    terms = st.checkbox("I agree to the terms and conditions")

    # Submit Button
    if st.button("Register"):
        if not full_name or not email or gender == "Select" or not terms:
            st.error("Please fill out all required fields and accept the terms.")
        else:
            user_data={
             'full_name':full_name,
             'email':email,
             'gender':gender,
             'dob':str(dob)  }  
            collection.insert_one(user_data)
            st.success(f"🎉 Registration successful! Welcome, {full_name}.")


        

if __name__ == "__main__":
    main()
    
