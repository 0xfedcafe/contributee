import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# Adjust colors and fonts here
text_color_light = "#8D8C8A"
font_family = "Arial, sans-serif"

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

centered_subtitle_html = f"""
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; margin: -20px; font-size: 26px; color: {text_color_light}; 
        font-family: {font_family};">Your donation matters. Donate to transform lives in rural villages!</h1>
    </div>
"""

descr1 = f"""
    <div style="color: {text_color_light}; font-family: {font_family}; text-align: center;">
        <p>Hope Haven - Kenya</p>
        <p>Nestled in the rural outskirts of Nairobi, Kenya, Hope Haven is home to 500 resilient individuals.</p>
        <p>However, with an 80% poverty rate, this village faces challenges in accessing clean water and educational resources.</p>
        <p>Your support can bring hope and positive change to the lives of its residents.</p>
    </div>
"""
descr2 = f"""
    <div style="color: {text_color_light}; font-family: {font_family}; text-align: center;">
        <p>Tranquil Meadows - India</p>
        <p>Located in the remote mountains of Himachal Pradesh, India, Tranquil Meadows is a picturesque village with 300 inhabitants.</p>
        <p>Despite its breathtaking landscapes, the village grapples with a 75% poverty rate and lacks essential healthcare facilities.</p>
        <p>Your contribution can make a lasting impact on the well-being of this community.</p>
    </div>
"""

descr3 = f"""
    <div style="color: {text_color_light}; font-family: {font_family}; text-align: center;">
        <p>Unity Village - Sierra Leone</p>
        <p>Situated in the coastal region of Sierra Leone, Unity Village is home to 700 individuals striving for a better life.</p>
        <p>With an 85% poverty rate, the village faces economic hardships and inadequate infrastructure.</p>
        <p>Your support can empower the residents of Unity Village and contribute to a brighter future.</p>
    </div>
"""

# Consts
images = ["vil1.jpg", "vil2.jpg", "vil3.jpg"]
descriptions = [descr1, descr2, descr3]
width_const = 700
fundraiser_names = ["amogus", "aboba", "test"]
wallet_names = ["32189321983", "543758435", "321321"]

# Create a session state to persist the current_index
current_index = st.session_state.get("current_index", 0)

st.markdown(f"""
    <h1 style="display: flex; justify-content: center;
    text-align: center; margin: -25px; font-size: 50px; font-family: sans-serif; color: {text_color_light}; 
    font-family: {font_family};"> <b>Make a donation!</h1>
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
centered_string = f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <p style="text-align: center; font-size: 18px; margin: 0px;">{descriptions[current_index]}</p>
    </div>
"""

st.markdown(centered_string, unsafe_allow_html=True)

# Wallet display
wallet_number = "EE32183921839213821"
wallet_string = f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <p style="text-align: center; font-size: 18px; color: {text_color_light}; font-family: {font_family};">
        Wallet number: {wallet_number}</p>
    </div>
"""
st.markdown(wallet_string, unsafe_allow_html=True)
# Fundraiser display
fundraiser_string = f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <p style="text-align: center; font-size: 20px; color: {text_color_light}; margin: 0px"><b>Name of fundraiser: {fundraiser_names[current_index]}</p>
    </div>
"""
st.markdown(fundraiser_string, unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.2, 0.13, 0.2])

with col2:
    # Wallet display
    wallet_number = "EE32183921839213821"
    wallet_string = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <p style="text-align: center; font-size: 18px; color: {text_color_light};"><b>Wallet number: {wallet_names[current_index]}</p>
        </div>
    """
    st.markdown(wallet_string, unsafe_allow_html=True)

    with st.expander("Make a donation"):
        donation_amount = st.text_input("Enter donation amount:", value="")

        # Add a button inside the expander
        donate = st.button("Send funds")

        if donate:
            if donation_amount.isdigit(): # Send to back-end
                st.success(f"Donation of {donation_amount} received!")
            else:
                st.error(f"Invalid amount: {donation_amount}!")