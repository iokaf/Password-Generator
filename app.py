"""This is the main file of the application."""
import streamlit as st
from src import create_window, about

with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Go to",
        ("About", "Password Generator")
    )

if page == "About":
    about()
else:
    create_window()