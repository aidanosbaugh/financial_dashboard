import time
import streamlit as st
import pandas as pd

from src.portfolio import (
    load_portfolio,
    total_profit,
    total_value,
    original_total,
)
from src.charts import allocation_chart
from src.data import update_prices
from src.portfolio import save_portfolio

st.set_page_config(
    page_title="Portfolio Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

stocks = load_portfolio()

st.image("assets/logo.png", width=250)

st.title("Financial Dashboard")

st.divider()

st.subheader("Holdings")

st.markdown(
    """
    <style>

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #161B22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 15px;
    }

    [data-testid="stMetricLabel"] {
        color: #8b949e;
        font-size: 14px;
    }

    [data-testid="stMetricValue"] {
        color: white;
        font-size: 28px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)

df = pd.DataFrame(stocks)

df["Value"] = df["Price"] * df["Shares"]

df["Gain/Loss"] = (df["Price"] - df["Original Price"]) * df["Shares"]

df["Return"] = (df["Gain/Loss"] / (df["Original Price"] * df["Shares"]) * 100)

df["Allocation"] = (df["Value"] / df["Value"].sum() * 100)

styled_df = (
    df.style
    .format({
        "Price": "${:.2f}",
        "Value": "${:,.2f}",
        "Gain/Loss": "${:,.2f}",
        "Return": "{:.2f}%",
        "Allocation": "{:.2f}%"
    })
    .background_gradient(
        subset=["Return"],
        cmap="RdYlGn",
        vmin=-20,
        vmax=20
    )
    .background_gradient(
        subset=["Gain/Loss"],
        cmap="RdYlGn",
        vmin=-1000,
        vmax=1000
    )
)

st.dataframe(
    styled_df,
    use_container_width=True
)


if st.sidebar.button("Refresh Prices"):

    st.sidebar.write("Updating prices...")
    
    stocks = update_prices(stocks)

    st.sidebar.write("Portfolio Updated!", )

    save_portfolio(stocks)

    time.sleep(1.25)

    st.rerun()

st.divider()

st.subheader("Portfolio Overview")
col1, col2, col3 = st.columns(3)
gain = (total_profit(stocks) / original_total(stocks)) * 100

with col1: 
    st.metric(
    label="Portfolio Value",
    value=f"${total_value(stocks):,.2f}"
)
with col2:
    st.metric(
        "Total Gain",
        f"${total_profit(stocks):.2f}", 
        delta=f"{gain:.2f}%"

    )
with col3:
    st.metric(
        "Return",
        f"{gain:.2f}%"
    )

st.divider()

