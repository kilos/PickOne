#!/usr/bin/python
import numpy
import scipy
import datetime
import Config

def main():
  tickers = readTickerFile(Config.TickerFilePath)
  for t in tickers:
    ts = getStockPrice(t, Config.TimeBegin, Config.TimeEnd)
    res = analyzer(ts)
  return 0

def readTickerFile(filepath):
  lst = []
  with open(filepath, 'r') as f:
    for line in f:
      line = line.rstrip()
      if line[0] == '#':
        continue
      lst.append(line)

  return lst