import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from watched import getMovieList
from datavis import decades

st.set_page_config(layout="wide")
if "selected_view" not in st.session_state:
    st.session_state.selected_view = None

fileUploaded = st.file_uploader("Upload your letterboxd data", type = ["csv"])

if fileUploaded is not None:
    movieList = getMovieList(fileUploaded)
    visualizations = {
        "Decades Breakdown": lambda: decades(movieList),
        "Rating Distribution": lambda: decades(movieList),
        "Movies Per Year": lambda: decades(movieList),
    }
    st.subheader("Choose what you  wish to see")
    cols = st.columns(3)
    labels = list(visualizations.keys())

    for i, label in enumerate(labels):
        col = cols[i % 3]
        with col:
            if st.button(label, use_container_width=True):
                st.session_state.selected_view = label

    st.divider()

    if st.session_state.selected_view:
        st.subheader(st.session_state.selected_view)
        fig = visualizations[st.session_state.selected_view]()
        st.pyplot(fig)