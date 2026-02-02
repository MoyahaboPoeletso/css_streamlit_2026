# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Moyahabo Poeletso Tshipepele")

# Collect basic information
name = "Moyahabo Poeletso Tshipepele"
field = "Computer Information Systems Graduate"
institution = "University of the Free State" 

summary = """A dedicated University of the Free State Computer Information Systems graduate with strong foundational 
skills in SQL development, C# programming, database management, and systems analysis. I have practical 
experience working in Linux environments through my High-Performance Computing module, where I 
gained hands-on exposure to system configuration and technical problem-solving. My degree integrates IT 
and business, enabling me to analyse systems, support digital operations, and understand organisational 
processes. I also contributed to the UFS Career Bridge project by documenting system features, testing 
functionalities, and supporting digital platform development. I am eager to apply my analytical and 
technical skills in dynamic, technology-driven environments while contributing to innovative digital 
solutions and continuous improvement"""


# Display basic profile information
st.header(" PROFESSIONAL SUMMARY")
st.write(f" {summary}")
st.write("Computer Information Systems")
st.write(f"**Institution:** {institution}")

st.image(
    "1c6e2295-1e6f-4942-8010-a414c3ae46e3.jpg",
    caption=""
)

# Add a section for publications



# Add a contact section
st.header("Contact Information")
email = "poeletsomoyahabo@gmail.com"



st.write(f"You can reach {name} at {email} ")



