import streamlit as st

st.title("Student Registration Form")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)
gender = st.radio("Select your gender", ["Male", "Female", "Other"])
course = st.selectbox(
    "Select your course",
    ["BCA", "B.Sc Computer Science", "B.Com", "BA"]
)
dob = st.date_input("Date of Birth")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

if st.button("Register"):
    st.success("Student Registration Successful!")

    st.write("### Student Details")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Course:", course)
    st.write("Date of Birth:", dob)
    st.write("Email:", email)
    st.write("Phone:", phone)
