import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('Bitcoin_data.csv', parse_dates=True, index_col=0)

# type is candle chart, mav is moving avarage(dates), include volume
mpf.plot(df, type='candle', mav=(100))