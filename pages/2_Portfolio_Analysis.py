import streamlit as st
import pandas as pd

from src.portfolio import load_portfolio
from src.charts import allocation_chart


stocks = load_portfolio()

df = pd.DataFrame(stocks)

fig = allocation_chart(df)

st.plotly_chart(
    fig,
    use_container_width=True
)