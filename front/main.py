import streamlit as st
import hmac


def main():
    login()

def login():
    def check_password():
        def password_entered():
            if hmac.compare_digest(st.session_state["password"], "aboba"):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # Don't store the password.
            else:
                st.session_state["password_correct"] = False

        # Return True if the password is validated.
        if st.session_state.get("password_correct", False):
            return True

        # Show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        if "password_correct" in st.session_state:
            st.error("😕 Password incorrect")
        return False

    if not check_password():
        st.stop()  # Do not continue if check_password is not True.

    # Main Streamlit app starts here
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")


if __name__ == "__main__":
    main()