import streamlit as st

option = st.radio(
    "Choose your favorite color:",
    ["Red", "Green", "Blue"]
)

st.write("You selected:", option)
