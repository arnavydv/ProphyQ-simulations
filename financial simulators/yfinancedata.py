import yfinance as yf
import pandas

data=yf.download("TSLA",start="2023-06-19",end="2026-06-19")
data.dropna()
data=data.drop("Ticker")
final=data.to_csv(r"C:\Users\Admin\Desktop\PROPHYQ\financial simulators\tsla.csv")
