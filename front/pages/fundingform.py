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

# Collect data from the user
form_data = {
    'fundraiser': st.text_input("Fundraiser name:", placeholder="", max_chars=40),
    'recipient': st.text_input("Recipient:", placeholder="", max_chars=40),
    'description': st.text_area("Description:", placeholder="", max_chars=350),
    'img': st.file_uploader("Image (Optional):")
}

submit = st.button("Submit form!")

if submit and not (form_data[0] or form_data[1] or form_data[2]):
    st.text("Please fill out the form!")
elif submit:
    requests.post(url=back_url, data=form_data)