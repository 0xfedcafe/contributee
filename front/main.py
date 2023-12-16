import streamlit as st
import requests

url = "https://backend"

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)


def make_post_request(data):
    response = requests.post(url, data=data)
    return response


def login_page():
    st.markdown('<b><p class="big-font">Welcome to Contributee<p>', unsafe_allow_html=True)
    user_input = st.text_input("Enter card value", type="password", key="password")
    submit_button = st.button("Submit")

    if submit_button:
        make_post_request(user_input)


def main():
    login_page()


if __name__ == "__main__":
    main()