import streamlit as st
import numpy as np 
import altair as alt
import pandas as pd

st.title("Web App")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"])
st.map(df)
