import streamlit as st

st.header("Contact Information ")

with st.form(key="email_form"):
    st.text_input("Your Email Address")
    st.text_area("your Message here!!")
    Button = st.form_submit_button("Submit")
    if Button:
        print("i am pressed")