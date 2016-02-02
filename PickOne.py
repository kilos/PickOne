#!/usr/bin/python
import numpy
import scipy
from datetime import datetime
import Config
import Data
import Analyzer
import Hurst

def main():
  tickers = Data.readTickerFile(Config.TickerFilePath)
  year, month, day = map(int, Config.TimeBegin.split('-'))
  tsBeg = datetime(year, month, day)
  year, month, day = map(int, Config.TimeEnd.split('-'))
  tsEnd = datetime(year, month, day)
  for t in tickers:
    ts = Data.getStockPrices(t, tsBeg, tsEnd)
    ts = ts['Adj Close']
    res = Analyzer.adfullerTest(ts)
    print t + ' Ad Fuller Test = ' 
    print res

    res = Hurst.hurst(ts)
    print t + ' Hurst = %f' %res
  return 0

if __name__ == '__main__':
  main()