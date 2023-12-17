import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

text_color_light = "#8D8C8A"

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 1rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

title = f"""
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; color: {text_color_light}; font-size: 45px;">Crypto Exchange</h1>
    </div>
"""

st.markdown(title, unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.4, 0.3, 0.3])
with col1:
    st.selectbox("From:", ("USD", "Peso", "Sol"))
with col2:
    st.selectbox("To:", ("BTC", "Etherium", "Dogecoin"))
# Balance, exchange rate, available traders, location