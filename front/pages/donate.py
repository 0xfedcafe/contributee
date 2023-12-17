import streamlit as st

centered_title_html = """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="text-align: center;">Make a donation!</h1>
    </div>
"""

centered_subtitle_html = """
    <div style="display: flex; justify-content: center; align-items: center;">
        <h1 style="text-align: center; font-size: 20px;">Donate to transform lives in rural villages!</h1>
    </div>
"""

# Dummy data representing poor villages
descr1 = """Hope Haven - Kenya 
Nestled in the rural outskirts of Nairobi, Kenya, Hope Haven is home to 500 resilient individuals. 
However, with an 80% poverty rate, this village faces challenges in accessing clean water and educational 
resources. Your support can bring hope and positive change to the lives of its residents."
"""
descr2 = """Tranquil Meadows - India \n
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

# List of image paths or URLs
images = ["vil1.jpg", "vil2.jpg", "vil3.jpg"]
descriptions = [descr1, descr2, descr3]
width_const = 800
col1, col2, col3 = st.columns(3)
custom_css = """
        <style>
            /* Example: Change the font to 'Arial, sans-serif' */
            body {
                font-family: 'Arial', sans-serif;
            }
        </style>
    """

def poor_village_image():

    # Create a session state to persist the current_index
    current_index = st.session_state.get("current_index", 0)

    with col1:
        if st.button("◀️ Previous", use_container_width=True):
            current_index = (current_index - 1) % len(images)

    with col2:
        st.write("")

    with col3:
        if st.button("Next ▶️", use_container_width=True):
            current_index = (current_index + 1) % len(images)

    st.session_state.current_index = current_index

    st.image(images[current_index], use_column_width=True)
    st.text(descriptions[current_index])

st.markdown(centered_title_html, unsafe_allow_html=True)
st.markdown(centered_subtitle_html, unsafe_allow_html=True)

poor_village_image()
