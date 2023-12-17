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

title = f"""
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; color: {text_color_light}; font-family: {font_family}; font-size: 45px;">
        Crypto Exchange</h1>
    </div>
"""

st.markdown(title, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    offer = st.button("Add offer", use_container_width=True)
    if offer:
        switch_page("addoffer")

curs = [("BTC", "UAH", 2, "https://backend.com"), ("ETH", "RUB", 3, "test"), ("DC", "USD", 10, "test"), ("ETH", "aa", "100", "test"), ("BTC", "UAH", 2, "test"),
        ("ETH", "RUB", 3, "test"), ("ETH", "USD", 10, "test"), ("ETH", "SEK", "100", "test")]
cols = len(curs) // 4

cls = [col1, col2, col3, col4] = st.columns([1, 1, 1, 1])
i = 0

st.markdown(
    """
    <style>
        .centered-column {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            border: 3px solid red; /* Set border style and color for columns */
            padding: 10px; /* Add padding for better appearance */
            margin-bottom: 4px; /* Add bottom margin */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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

for a in range(cols):
    for i in range(4):
        with cls[i]:
            st.markdown(
                f"""
                <div class="centered-column">
                    <h1 style="text-align:center">1{curs[i+4*a][0]}</h1>
                    <h1 style="text-align:center; font-size:25px;">=</h1>
                    <h1 style="text-align:center">{curs[i+4*a][2]}{curs[i+4*a][1]}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(centered_button, unsafe_allow_html=True)
            button_clicked = st.button(f"BUY {curs[i+4*a][2]}{curs[i+4*a][0]}", i+4*a)

            if button_clicked:
                requests.post("...")