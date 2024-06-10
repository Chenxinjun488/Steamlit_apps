import pandas as pd
import streamlit as st 
from pygwalker.api.streamlit import StreamlitRenderer


uploaded_file = st.file_uploader("Your csv file")

if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()