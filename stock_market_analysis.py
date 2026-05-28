import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from curl_cffi import requests
1
session = requests.Session(impersonate = "chrome")

st.title("Stock market Data Analysis")

ticker_symbol = st.text_input("Enter the stock ticker symbol (e.g., AAPL, MSFT, GOOGL):", "AAPL") # Default value is set to "AAPL"

ticker_data = yf.Ticker(ticker_symbol)

#start_date = pd.to_datetime("2020-01-01")
#end_date = pd.to_datetime("today")

start_date = st.date_input("Start Date:", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date:", value=pd.to_datetime("today"))

ticker_df = ticker_data.history(start=start_date, end=end_date)

st.dataframe(ticker_df)

st.write(f"Closing Price of {ticker_symbol} from {start_date} to {end_date}:")
st.line_chart(ticker_df["Close"])

st.write(f"Volume of {ticker_symbol} from {start_date} to {end_date}:")
st.line_chart(ticker_df["Volume"])

col1, col2 = st.columns(2)

with col1: 
    st.write(f"Open Price of {ticker_symbol} from {start_date} to {end_date}:")
    st.line_chart(ticker_df["Open"])

with col2: 
    st.write(f"High Price of {ticker_symbol} from {start_date} to {end_date}:")
    st.line_chart(ticker_df["High"])

#Exponential MOving Average (EMA)
st.write(f"Exponential Moving Average (EMA) of {ticker_symbol} from {start_date} to {end_date}")

alpha = st.slider("Select the alpha value for EMA:", min_value=0.01, max_value=1.0, value=0.1, step=0.01)

#Calculate EMA
ema_values = []
ema = ticker_df["Close"].iloc[0]
ema_values.append(ema)

for n in range(1, len(ticker_df)):
    ema = alpha * ticker_df["Close"].iloc[n] + (1 - alpha) * ema
    ema_values.append(ema)

ticker_df["EMA"]= ema_values

st.line_chart(ticker_df[["Close","EMA"]])

#num = st.number_input("Enter the number of recent days to display:", min_value=1, max_value=len(ticker_df), value=5)

num = st.number_input("Enter a number:", min_value =1 , max_value =100, value =5)
if st.button("Calculate Square"):
    result = num ** 2
    st.write(f"The square of {num} is {result}!") 