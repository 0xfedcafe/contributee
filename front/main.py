import streamlit as st
import requests

url = "https://backend.com"
st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

centered_welcome_title_html = """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="text-align: center;"><b>Welcome to cotributee</h1>
    </div>
"""


def make_post_request(data):
    response = requests.post(url, data=data)
    print(data)
    return response


def login_page():
    st.markdown(centered_welcome_title_html, unsafe_allow_html=True)
    user_input = st.text_input("Enter your card number here", type="password", key="password")

    col1, col2, col3 = st.columns([0.45, 0.14, 0.45])

    with col2:
        login_button = st.button("Log in", use_container_width=True)

    if login_button:
        make_post_request(user_input)


def main():
    login_page()


if __name__ == "__main__":
    main()
