import streamlit as st
import pandas as pd
from PIL import Image

### --- SET CONFIGURATION
st.set_page_config(
    page_title="Copymining Review Word Counter",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

### --- CREATE SIDEBAR
with st.sidebar:
    logo = "https://raw.githubusercontent.com/mr-emreerturk/review_word_counter/master/streamlit_app/emf_media_logo.png"
    st.image(logo, output_format="png")
    st.header("The App")
    st.markdown(
        """
    This app has one purpose: With this app you can scrape as many Amazon Reviews as you want.
    """
    )
    st.header("How to use:")
    st.markdown(
        """
    1. Paste the Amazon Product Page into the designated field.
    2. Add up to 15 links by clicking 'add link'.
    3. Press 'execute' to start the scraping.
    4. Once finished running, download the csv file and import into an excel file.
    """
    )
    st.header("Tutorial")
    # TODO: Add st.video for video tutorial

st.title("Amazon Review Scraper")
