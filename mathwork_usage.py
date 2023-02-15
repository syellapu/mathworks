import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Mathworks_Report",
                   page_icon=":bar_chart:",
                   layout="wide")
st.header("Mathworks Statistics Usage Report")

df = pd.read_excel('Mathworks_monthly_data_report.xlsx', usecols='A:D')
st.dataframe(df)

st.sidebar.header("Please filter here: ")
dept = st.sidebar.multiselect(
    "Select the department here :",
    options=df["dept"].unique(),
)

df_selection = df.query(
    "dept == @dept"
)
st.dataframe(df_selection)

