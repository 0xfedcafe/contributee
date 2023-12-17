import streamlit as st

st.set_page_config(layout="wide")

centered_subtitle_html = """
    <div style="white-space: nowrap; display: inline; justify-content: center; align-items: center;">
        <h1 style="text-align: center; margin: -25px; font-size: 50px;">Make a donation!</h1>
        <h1 style="text-align: center; margin: -25px; font-size: 30px;">Donate to transform lives in rural villages!</h1>
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
width_const = 800

# Create a session state to persist the current_index
current_index = st.session_state.get("current_index", 0)

st.markdown(centered_subtitle_html, unsafe_allow_html=True)

col0, col1, col2, col3, col4 = st.columns(5)

with col0:
    if st.button("◀️ Previous", use_container_width=True):
        current_index = (current_index - 1) % len(images)

with col4:
    if st.button("Next ▶️", use_container_width=True):
        current_index = (current_index + 1) % len(images)

st.session_state.current_index = current_index

st.image(images[current_index], width=width_const, use_column_width=True)

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

col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col2:
    donate = st.button("Make a donation!", use_container_width=True)
    if donate:
        print("Hello!")