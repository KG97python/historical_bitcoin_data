import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

# this is the code I used to manipulate the data into being useful for matplotlib finance.
# There is most likely a more efficient way of doing this. I will be back once i have found it.

dates = []
opens = []
highs = []
lows = []
closes = []
volumes = []

df = pd.read_csv('Bitcoin_datas.csv')
date = df['Date']
opened = df['Open']
high = df['High']
low = df['Low']
close = df['Close']
volume = df['Volume']

def reverse_date():
    for i in date:
        dates.append(i)
    dates.reverse()
    df['Date'] = dates

    for i in opened:
        opens.append(i)
    opens.reverse()
    df['Open'] = opens

    for i in high:
        highs.append(i)
    highs.reverse()
    df['High'] = highs

    for i in low:
        lows.append(i)
    lows.reverse()
    df['Low'] = lows

    for i in close:
        closes.append(i)
    closes.reverse()
    df['Close'] = closes

    for i in volume:
       volumes.append(i)
    volumes.reverse()
    df['Volume'] = volumes

    df.to_csv('____.csv')

reverse_date()
