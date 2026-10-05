import streamlit as st

st.title("Warning Message Program")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success("Submitted successfully!")
    else:
        st.warning("Warning: Please enter your name.")
