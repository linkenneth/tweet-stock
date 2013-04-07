from urllib2 import urlopen
from datetime import datetime
from pymongo import MongoClient

def __request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    return urlopen(url).read().strip().strip('"')

def get_price(symbol): 
    return __request(symbol, 'l1')

def get_historical_prices(symbol, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYYMMDD'
    Returns a nested list.
    """
    url = 'http://ichart.yahoo.com/table.csv?s=%s&' % symbol + \
          'd=%s&' % str(int(end_date[4:6]) - 1) + \
          'e=%s&' % str(int(end_date[6:8])) + \
          'f=%s&' % str(int(end_date[0:4])) + \
          'g=d&' + \
          'a=%s&' % str(int(start_date[4:6]) - 1) + \
          'b=%s&' % str(int(start_date[6:8])) + \
          'c=%s&' % str(int(start_date[0:4])) + \
          'ignore=.csv'
    days = urlopen(url).readlines()
    data = [day[:-2].split(',') for day in days][1:]
    return data

def save_price(entry, coll):
    shit = {
        "date" : datetime.strptime(entry[0], "%Y-%m-%d"),
        "price" : int(entry[4])
    }
    coll.save(shit)
