import streamlit as st

password = st.text_input("Enter your password", type="password")

if password:
    st.write("Password entered successfully!")
