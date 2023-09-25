import streamlit as st
st.set_page_config(layout="wide")  # web page get adjusted even when changing the webpage size and fits the screen
col1,col2=st.columns(2) # divide the web app  by two columns
with col1:
    st.image("images/photo.png")

with col2:
   st.title("Mohammed Arsac")
   comment="""I am  a  Python Programmer and an Entrepreneur """ # this is docstring used to have big content and can also have multiple lines.
   st.info (comment)
