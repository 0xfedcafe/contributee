import streamlit as st

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

col0, col1, col2, col3, col4 = st.columns([0.15, 0.25, 0.05, 0.25, 0.15])

with col0:
    st.text("")
with col1:
    st.selectbox("From:", ("USD", "Peso", "Sol"))
with col2:
    st.text("")
with col3:
    st.selectbox("To:", ("BTC", "Etherium", "Dogecoin"))
with col4:
    st.text("")

# Balance, exchange rate, available traders, location