import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests

back_url = ""

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

st.markdown("""<div>
                <h1 style="white-space: nowrap; text-align:center, display:inline;">Welcome to Contributee central hub!</h1>
            </div>""",
            unsafe_allow_html=True
            )

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown(centered_button, unsafe_allow_html=True)
    donations = st.button("Donations", use_container_width=True)
    st.markdown(centered_button, unsafe_allow_html=True)
    crypto = st.button("Cryptocurrency Exchange", use_container_width=True)
    if donations:
        switch_page("donate")
    elif crypto:
        switch_page("exchange")
