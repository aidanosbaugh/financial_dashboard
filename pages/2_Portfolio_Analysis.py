import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

from src.portfolio import load_portfolio
from src.data import get_history