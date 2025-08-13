import streamlit as stml

def apply_css(file_name):
    with open(file_name) as f:
        stml.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)