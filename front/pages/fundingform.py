import streamlit as st
import requests

title = """
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; font-size: 40px;">Fund those in need!</h1>
    </div>
"""
st.set_page_config(layout="wide")

st.markdown(title, unsafe_allow_html=True)

# Fields like first name, last name
fundraiser = st.text_input("Fundraiser name:", placeholder="", max_chars=15)
desc = st.text_input("Description:", placeholder="", max_chars=350)
rec = st.text_input("Recipient:", placeholder="", max_chars=15)
im = st.file_uploader("Image (Optional):")

submit = st.button("Submit form!")

if submit and (fundraiser, desc, rec, im is not None):
    requests.post("https://backend.com")
else:
    st.text("Please fill out the form!")