import streamlit as st

st.title("Error Message Program")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success("Submitted successfully!")
    else:
        st.error("Error: Please enter your name.")
