import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


centered_subtitle_html = """
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; margin: -20px; font-size: 26px;">Your donation matters. Donate to transform lives in rural villages!</h1>
    </div>
"""

descr1 = """Hope Haven - Kenya 
Nestled in the rural outskirts of Nairobi, Kenya, Hope Haven is home to 500 resilient individuals. 
However, with an 80% poverty rate, this village faces challenges in accessing clean water and educational 
resources. Your support can bring hope and positive change to the lives of its residents."
"""
descr2 = """Tranquil Meadows - India
Located in the remote mountains of Himachal Pradesh, India, Tranquil Meadows is a picturesque 
village with 300 inhabitants. Despite its breathtaking landscapes, the village grapples with a 75% poverty rate 
and lacks essential healthcare facilities. Your contribution can make a lasting impact on the well-being of this 
community."
"""
descr3 = """Unity Village - Sierra Leone
Situated in the coastal region of Sierra Leone, Unity Village is home to 700 individuals 
striving for a better life. With an 85% poverty rate, the village faces 
economic hardships and inadequate infrastructure. Your support can empower the residents of Unity Village and 
contribute to a brighter future."
"""

# Consts
images = ["vil1.jpg", "vil2.jpg", "vil3.jpg"]
descriptions = [descr1, descr2, descr3]
width_const = 700

# Create a session state to persist the current_index
current_index = st.session_state.get("current_index", 0)

st.markdown("""
    <h1 style="display: flex; justify-content: center;
    text-align: center; margin: -25px; font-size: 50px; font-family: sans-serif;"><b>Make a donation!</h1>
""", unsafe_allow_html=True)

col0, col1, col2, col3, col4 = st.columns([0.2, 0.05, 0.75, 0.05, 0.2])

with col1:
    st.markdown("""<div style="margin:250px"></div>""", unsafe_allow_html=True)  # Add an empty space as a placeholder
    if st.button("◀️", use_container_width=True, key="prev_button"):
        current_index = (current_index - 1) % len(images)

with col2:
    st.markdown(centered_subtitle_html, unsafe_allow_html=True)
    st.image(images[current_index], width=width_const, use_column_width=True)

with col3:
    st.markdown("""<div style="margin:250px"></div>""", unsafe_allow_html=True)  # Add an empty space as a placeholder
    if st.button("▶️", use_container_width=True):
        current_index = (current_index + 1) % len(images)

st.session_state.current_index = current_index


# Display text
centered_string= f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <p style="text-align: center; font-size: 18px; margin: 0px">{descriptions[current_index]}</p>
    </div>
"""

st.markdown(centered_string, unsafe_allow_html=True)

# Wallet display
wallet_number = "EE32183921839213821"
wallet_string = f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <p style="text-align: center; font-size: 18px;">Wallet number: {wallet_number}</p>
    </div>
"""
st.markdown(wallet_string, unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.2, 0.13, 0.2])

with col2:
    with st.expander(label="Make a donation!"):
        # Add a text input field
        donation_amount = st.text_input("Enter donation amount:", value="")

        # Add a button inside the expander
        donate = st.button("Send funds")

        if donate:
            print("Hello!")
            st.success(f"Donation of {donation_amount} received!")