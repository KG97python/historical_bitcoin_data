import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

# Created a different module for the chart because I plan on improving it in the future with a Gui.
# The user will be able to enter the specific dates they want to see plus the moving average of their choice.

style.use('ggplot')

df = pd.read_csv('bitcoin_data.csv', parse_dates=True, index_col=0)

# type is candle chart, mav is moving average(dates)
mpf.plot(df, type='candle', mav=(50, 100))