import streamlit as st
import plotly.express as px
from src.portfolio import load_portfolio, get_portfolio_history
from src.data import get_history
import plotly.graph_objects as go

st.title("Benchmark")

stocks = load_portfolio()

tickers = [
    stock["Ticker"]
    for stock in stocks
]



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

portfolio = get_portfolio_history(stocks, timeframes[selected_time])

spy = get_history(
    "SPY", 
    timeframes[selected_time]
)


## Normalize data into percentage growth
portfolio["Normalized"] = portfolio / portfolio.iloc[0] * 100
spy["Normalized"] = (
    spy["Close"] / spy["Close"].iloc[0]
) * 100

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=portfolio.index,
        y=portfolio["Normalized"],
        name="Portfolio"
    )
)
fig.add_trace(
    go.Scatter(
        x=spy.index,
        y=spy["Normalized"],
        name="SPY"
    )
)
fig.update_layout(
    title="S&P Benchmark Comparision",
    xaxis_title="Date",
    yaxis_title="Growth (100 = Starting Value)"
)
st.plotly_chart(fig, use_container_width=True)

