import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests

back_url = ""
# Adjust colors and fonts here
text_color_light = "#8D8C8A"
font_family = "Arial, sans-serif"

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 1rem;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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

title = f"""
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; color: {text_color_light}; font-family: {font_family}; font-size: 45px;">
        Crypto Exchange</h1>
    </div>
"""

st.markdown(title, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    offer = st.button("Return to offers", use_container_width=True)
    if offer:
        switch_page("exchange")

    data = {
        st.text_input("Currency to sell:"),
        st.text_input("Exchange rate:"),
        st.text_input("Currency to buy:")
    }

    centered_button = """
        <style>
            div.stButton > button {
                display: block;
                margin: 0 auto;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                border: 3px solid red; /* Set border style and color for buttons */
                padding: 10px; /* Add padding for better appearance */
            }
        </style>
    """
    st.markdown(centered_button, unsafe_allow_html=True)
    button_clicked = st.button("Request exchange")

    if button_clicked:
        requests.post(url=back_url, data=data)
