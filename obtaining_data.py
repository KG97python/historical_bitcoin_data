from datetime import datetime
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import requests
import lxml
import csv

# this module contains the code that I will be using to extract the data I will need for this project.

dates = []
opens = []
highs = []
lows = []
close = []
volumes = []

def collect_data():
    resp = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20100428&end=20200204')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    # "Table" in coinmarketcap is not named, So i find the div before it.
    table = soup.find('div', {'class': 'cmc-table__table-wrapper-outer'})
    # then I tell bs4 to find the tbody after that.
    table_sorted = table.find_next('tbody')

    # did this to turn the data into integers to make it easy to work with.
    # Probably not the most efficient way of doing it, but it worked.

    for row in table_sorted.findAll('tr'):
        date = row.findAll('td')[0].text
        comma = date.replace(',', '')
        result = comma.replace(' ', '-')
        converted = datetime.strptime(result, '%b-%d-%Y')
        print(converted)
        dates.append(converted)

        opened = row.findAll('td')[1].text
        remove = opened.replace(',', '')
        integer = float(remove)
        opens.append(integer)


        high = row.findAll('td')[2].text
        remove1 = high.replace(',', '')
        integer1 = float(remove1)
        highs.append(integer1)

        low = row.findAll('td')[3].text
        remove2 = low.replace(',', '')
        integer2 = float(remove2)
        lows.append(integer2)

        closed = row.findAll('td')[4].text
        remove3 = closed.replace(',', '')
        integer3 = float(remove3)
        close.append(integer3)

        volume = row.findAll('td')[5].text
        remove4 = volume.replace(',', '')
        integer4 = float(remove4)
        volumes.append(integer4)

def create_csv():
    with open("Bitcoin_data.csv", 'w', newline='') as f:
        columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        the_writer = csv.DictWriter(f, fieldnames=columns)
        the_writer.writeheader()
        n = 0
        for i in range(2474):
            the_writer.writerow({'Date': dates[n], 'Open': opens[n], 'High': highs[n], 'Low': lows[n],
                                 'Close': close[n], 'Volume': volumes[n]})
            n += 1


def main_loop():
    collect_data()
    create_csv()