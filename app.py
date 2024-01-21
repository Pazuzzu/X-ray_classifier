from inference import *
import os

import streamlit as st

OUTPUT_DIR = 'temp/'
# Clean temp folder
for f in os.listdir(OUTPUT_DIR):
    os.remove(os.path.join(OUTPUT_DIR, f))

# Title
st.markdown("<h1 style='text-align: center; color: black;'>X-ray image classifier 🩻</h1>", unsafe_allow_html=True)
# Credit
st.write(
    """
    by *Pazuzzu*
    """)

st.write("""
         #
         """)

# Layout
container = st.container()
col1, col2, col3, col4 = st.columns(4)

# Upload Button
st.write("""
        #
        #
        """)
label = 'Upload a photo to classify'
uploaded_img = st.file_uploader(label,
                                type=['png', 'jpg', 'jpeg'] , 
                                accept_multiple_files=False, 
                                key=None, 
                                help=None, 
                                on_change=None, 
                                args=None, 
                                disabled=False, label_visibility="visible")


if uploaded_img is not None:
    img_file = uploaded_img

    # Inference
    # prediction, proba = predict_from_image_bytes(img_file.getvalue()) #prediction from bytes buggy, fix and use later
    # Temporary Workaround a round : Save to img and use predict_from_image_path
    img_path = OUTPUT_DIR + img_file.name
    with open(img_path, 'wb') as f : f.write(img_file.getbuffer())
    prediction, proba = predict_from_image_path(img_path)

    proba = f'{proba * 100}%'
    st.success('Classified')

    with container:
        # Preview Image
        with st.columns(3)[1]:
            st.image(img_file, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        st.write("""
                #
                """)
        # Preview results
        with col1:
            st.markdown(f"<h3 style='text-align: left; color: gray;'>Label :</h3>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<h4 style='text-align: left; color: green; font-weight: bold;'>{prediction}</h4>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<h3 style='text-align: left; color: gray;'>Confidance :</h3>", unsafe_allow_html=True)
        with col4:
            st.markdown(f"<h4 style='text-align: left; color: green; font-weight: bold;'>{proba}</h4>", unsafe_allow_html=True)
