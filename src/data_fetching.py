import yfinance as yf
import pandas as pd
from datetime import datetime
def fetch_btc_data():
      data = yf.download('BTC-USD', 
                        start='2020-01-01', 
                        end=datetime.today().strftime('%Y-%m-%d'))
      return data
if __name__ == '__main__':
      btc_data = fetch_btc_data()
      btc_data.to_csv('data/bitcoin_data.csv')