import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv",sep=",")

st.set_page_config(layout="wide")
st.title("Night Striker - A GateWay to Extreme Thrill")
content = """Introducing Night Striker, where innovation meets elegance in the world of automotive excellence. Our 
brand embodies a harmonious fusion of cutting-edge technology, unmatched performance, and timeless design. With a 
legacy steeped in precision engineering, Night Striker cars redefine the art of driving, setting new standards for 
luxury and exhilaration on every journey. Join us on a captivating exploration of automotive mastery, where every 
curve, every detail, and every innovation reflects our unwavering commitment to redefining the driving experience. 
Welcome to Night Striker, where the road to automotive perfection begins."""
st.write(content)

st.subheader("Our Team")
col1,empty_col1, col2,empty_col2, col3 = st.columns([1.5,0.3,1.5,0.3
                                                        ,1.7])

with col1:
    for _,row in df[:4].iterrows():
        st.subheader(row["role"])
        first_name=row["first name"].capitalize()
        last_name=row["last name"].capitalize()
        st.write(first_name, last_name)
        st.image("images/" + row["image"])

with col2:
    for _,row in df[4:8].iterrows():
        st.subheader(row["role"])
        first_name = row["first name"].capitalize()
        last_name = row["last name"].capitalize()
        st.write(first_name, last_name)
        st.image("images/"+row["image"])

with col3:
    for _,row in df[8:].iterrows():
        st.subheader(row["role"])
        first_name = row["first name"].capitalize()
        last_name = row["last name"].capitalize()
        st.write(first_name, last_name)
        st.image("images/" + row["image"])
