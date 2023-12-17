import streamlit as st
import requests
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page

# Adjust colors and fonts here
text_color_dark = "#353638"
text_color_light = "#8D8C8A"
font_size = "20px"

url = "https://backend"
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="Contributee",
    page_icon=":heart:",
)

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>

"""

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

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

centered_welcome_title_html = f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="text-align: center; color: {text_color_light};"><b>Welcome to Contributee!</b></h1>
    </div>
"""

def make_post_request(data):
    response = requests.post(url, data=data)
    return response

def login_page():
    st.markdown(centered_welcome_title_html, unsafe_allow_html=True)

    # Add an empty line
    st.write("\n")

    user_input = st.text_input("Enter your card number here", type="password", key="password")

    # Add an empty line
    st.write("\n")
    st.write("\n")

    col1, col2, col3 = st.columns([0.45, 0.14, 0.45])

    with col2:
        login_button = st.button("Log in", use_container_width=True)

    if login_button:
        response = make_post_request({user_input})
        if response == True:
            switch_page("menu")
        else:
            st.error("Invalid credentials!")

def main():
    st.markdown("""<div style="margin:250px"></div>""", unsafe_allow_html=True)
    login_page()

if __name__ == "__main__":
    main()
