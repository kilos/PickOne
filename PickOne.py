#!/usr/bin/python
import numpy
import scipy
import datetime
import 

def main():
  tickers = readTickerFile()
  for t in tickers:
    ts = readData(t)
    res = analyzer(ts)
  return 0