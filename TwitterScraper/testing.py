import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime
from time import sleep

if "option" not in st.session_state:
    st.session_state["option"] = None


with st.form("input"):
    selected_options = st.sidebar.multiselect(
        "Select option:", ["Option1", "Option2", "Option3"], default="Option1")
    text = st.text_area("Paste text here", height=350)
    submit_button = st.form_submit_button(label="Extract data")

if submit_button:
    # Check that text field is not empty
    if not text.strip():
        st.error("WARNING: Please enter text")
    else:
        with st.spinner(text = "Extracting information…"):
            sleep(3)
            st.session_state["option"] = selected_options
            st.write("You selected: {} - inside submit_button".format(selected_options))
            st.write(text)

if st.session_state["option"] is not None:
    st.write("You selected: {} - outside submit_button".format(st.session_state["option"]))