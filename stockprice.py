import yfinance as yf
import streamlit as st
import pandas as pandas

st.title('Stock Price Visualizer')


#get data on this ticker
tickerDataGoogle = yf.Ticker('GOOGL')
tickerDataGamestop = yf.Ticker('GME')
tickerDataApple = yf.Ticker('AAPL')
tickerDataAmazon = yf.Ticker('AMZN')
tickerDataNetflix = yf.Ticker('NFLX')

#get the historical prices for this ticker
tickerDfGoogle = tickerDataGoogle.history(period='1d', start='2011-3-31', end='2021-03-31')
tickerDfGamestop = tickerDataGamestop.history(period='1d', start='2011-3-31', end='2021-03-31')
tickerDfApple = tickerDataApple.history(period='1d', start='2011-3-31', end='2021-03-31')
tickerDfAmazon = tickerDataAmazon.history(period='1d', start='2011-3-31', end='2021-03-31')
tickerDfNetflix = tickerDataNetflix.history(period='1d', start='2011-3-31', end='2021-03-31')

# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write('Google\'s closing price from March 31st 2011 - March 31st 2021')
st.line_chart(tickerDfGoogle.Close)

st.write('Gamestop\'s closing price from March 31st 2011 - March 31st 2021')
st.line_chart(tickerDfGamestop.Close)

st.write('Apple\'s closing price from March 31st 2011 - March 31st 2021')
st.line_chart(tickerDfApple.Close)

st.write('Amazon\'s closing price from March 31st 2011 - March 31st 2021')
st.line_chart(tickerDfAmazon.Close)

st.write('Netflix\'s closing price from March 31st 2011 - March 31st 2021')
st.line_chart(tickerDfNetflix.Close)
