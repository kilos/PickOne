# Import the Time Series library
import statsmodels.tsa.stattools as st

# Output the results of the Augmented Dickey-Fuller test for Google
# with a lag order value of 1
def adfullerTest(ts):
  return st.adfuller(ts, 1)

