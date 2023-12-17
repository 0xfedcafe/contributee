import streamlit as st
import requests
from datetime import datetime

back_url = "backend.com"
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Adjust colors and fonts here
text_color_light = "#8D8C8A"
font_family = "Arial, sans-serif"

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

title = f"""
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; font-size: 40px; color: {text_color_light}; font-family: {font_family};">
        Fund those in need!</h1>
    </div>
"""

st.markdown(title, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    [data-testid="collapsedControl"]{
        display: none;
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Fields like first name, last name
fundraiser = st.text_input("Fundraiser name:", placeholder="", max_chars=40)
rec = st.text_input("Recipient:", placeholder="", max_chars=40)
desc = st.text_area("Description:", placeholder="", max_chars=350)
im = st.file_uploader("Image (Optional):")

submit = st.button("Submit form!")

if submit and (fundraiser, desc, rec, im is not None):
    requests.post(url=back_url,
                  data={"fundraiser": fundraiser, "desc": desc, "rec": rec, "im": im, "date": datetime.now()})
else:
    st.text("Please fill out the form!")
