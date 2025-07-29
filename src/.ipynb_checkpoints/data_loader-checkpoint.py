import yfinance as yf
import pandas as pd

def download_prices_adj_close(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=False)["Adj Close"] #auto adjust important pour obtenir les prix de clotures ajustés
    return data