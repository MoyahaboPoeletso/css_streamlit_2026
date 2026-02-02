# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Moyahabo Poeletso's Profile")

# Collect basic information
name = "Moyahabo Poeletso Tshipepele"
field = "Computer Information Systems Graduate"
institution = "University of the Free State"


# Display basic profile information
st.header(" PROFESSIONAL SUMMARY")
st.write("")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "1c6e2295-1e6f-4942-8010-a414c3ae46e3.jpg",
    caption=""
)

# Add a section for publications



# Add a contact section
st.header("Contact Information")
email = "poeletso@gmail.com"

st.write(f"You can reach {name} at {email}.")