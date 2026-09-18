import streamlit as st

option = st.selectbox(
    "Choose a fruit:",
    ["Apple", "Banana", "Mango", "Orange"]
)

st.write("You selected:", option)
