import streamlit as st
import plotly.express as px
from src.portfolio import load_portfolio
from src.data import get_history

st.title("Stock Viewer")

stocks = load_portfolio()

tickers = [
    stock["Ticker"]
    for stock in stocks
]

ticker = st.selectbox(
    "Choose a Stock",
    tickers
)


timeframes = {
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "5 Years": "5y"
}


selected_time = st.selectbox(
    "Choose Timeframe",
    timeframes.keys()
)


history = get_history(
    ticker,
    timeframes[selected_time]
)


fig = px.line(
    history,
    x=history.index,
    y="Close",
    title=f"{ticker} Performance"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price $"
)


st.plotly_chart(
    fig,
    use_container_width=True
)