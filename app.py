# streamlit_app.py
import streamlit as st
import subprocess


subprocess.run(["python", "-m", "xbrl_us"], capture_output=True, text=True)


