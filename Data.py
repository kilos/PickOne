# Import Datetime and the Pandas DataReader
from datetime import datetime
from pandas_datareader.data import DataReader

# Download the Google OHLCV data from 1/1/2000 to 1/1/2013
def getStockPrices(ticker, beg, end):
  ts = DataReader(ticker, "yahoo", beg, end)
  return ts


def readTickerFile(filepath):
  lst = []
  with open(filepath, 'r') as f:
    for line in f:
      line = line.rstrip()
      if line[0] == '#':
        continue
      lst.append(line)

  return lst
