import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Mathworks_Report",
                   page_icon=":bar_chart:",
                   layout="wide")
st.header("Mathworks Statistics Usage Report")

df = pd.read_excel('Mathworks_monthly_data_report.xlsx', usecols='A:D')
df['dept'] = df['dept'].apply(str)

groupby_column = st.selectbox(
    'What would you like to analyse? ',
    ('id', 'dept', 'feature'),
)

output_columns = ['usage']
df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
#st.dataframe(df_grouped)

fig = px.bar(
    df_grouped,
    y='usage',
    color_continuous_scale=['red', 'yellow', 'green'],
    template='plotly_white',
    title=f'<b>Usage by {groupby_column}</b>'
)

#st.dataframe(df_grouped)
#st.plotly_chart(fig)

left_column, right_column = st.columns(2)
left_column.dataframe(df_grouped, use_container_width=True)
right_column.plotly_chart(fig, use_container_width=True)
