# stock-prediction
import yfinance as yf
sp500=yf.Ticker("^GSPC")
sp500=sp500.history(period="max")
sp500

