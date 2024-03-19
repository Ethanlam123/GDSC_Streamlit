import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from stocknews import StockNews

# Initialize session state variables
if 'ticker' not in st.session_state:
    st.session_state.ticker = []
if 'data' not in st.session_state:
    st.session_state.data = {}

# App title
st.title('💰STOCK Dashboard')

# Sidebar: Add or remove stock tickers
st.sidebar.title('Stock Ticker Options')
ticker_input = st.sidebar.text_input('Enter a stock ticker')
start_date = ...
end_date = ...

# Functions to manipulate tickers
def add_ticker():
    pass

# @st.cache_data
def remove_ticker(ticker_to_remove):
    pass

def display_stock_data(ticker):
    pass

def display_custom_plot(df):
    pass
    
def display_stock_news(ticker):
    pass

# Sidebar buttons for adding or removing tickers
# TODO

# Main content: Display stock data and news
if st.session_state.ticker:
    selected_ticker = st.selectbox('Select a ticker to view', st.session_state.ticker)
    display_stock_data(selected_ticker)
    display_stock_news(selected_ticker)
else:
    st.write('Please add a ticker to display data.')