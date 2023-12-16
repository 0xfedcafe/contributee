import streamlit as st
import pandas as pd

# Dummy data representing poor villages
centered_title_html = """
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <h1 style="text-align: center;">Make a donation!</h1>
    </div>
"""

centered_subtitle_html = """
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <h1 style="text-align: center;">Donate to trasform lives in rural villages!</h1>
    </div>
"""

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

def donate_to_village():
    st.markdown(centered_title_html, unsafe_allow_html=True)

    st.markdown(centered_subtitle_html, unsafe_allow_html=True)

def poor_village_image():
    # List of image paths or URLs
    images = ["vil1.jpg", "vil2.jpg", "vil3.jpg"]
    descriptions = [descr1, descr2, descr3]
    # current_index = st.slider("Select Image", 0, len(images) - 1, 0)

    # Display arrows for navigation
    col1, col2, col3 = st.columns(3)

    current_index = 0

    # Create a session state to persist the current_index
    current_index = st.session_state.get("current_index", 0)

    with col1:
        if st.button("◀️ Previous"):
            current_index = (current_index - 1) % len(images)

    with col2:
        st.write("")

    with col3:
        if st.button("Next ▶️"):
            current_index = (current_index + 1) % len(images)

    # Save the current_index to session state
    st.session_state.current_index = current_index

    st.image(images[current_index])
    st.text(descriptions[current_index])

def main():
    donate_to_village()
    poor_village_image()

if __name__ == "__main__":
    main()
