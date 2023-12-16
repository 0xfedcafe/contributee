import streamlit as st
import poetry as pt

def main():
    bg_color = "#000000"  # Change this to your desired color code
    css = f"""
        <style>
            body {{
                background-color: {bg_color};
            }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    st.title("My Streamlit App")
    st.write("This is a Streamlit app with a custom background color.")


if __name__ == "__main__":
    main()