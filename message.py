import streamlit as st

st.title("Message Success Program")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success("Message submitted successfully!")
    else:
        st.warning("Please enter your name.")
