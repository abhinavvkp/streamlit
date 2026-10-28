import streamlit as st

st.title("Number Input Example")

age = st.number_input("Enter your age:", min_value=0, max_value=100, step=1)

st.write("Your age is", age)
