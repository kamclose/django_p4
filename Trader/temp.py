import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = yf.download("BTC-USD", "2017-01-01")
dates = mdates.date2num(data.index.to_pydatetime())
plt.plot_date(dates, data['Adj Close'], '-')

plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())

plt.grid(True)
plt.ylabel(r'Price [$]')
plt.title('BTC-USD Price')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in plt.gca().get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

plt.show()

# info = yf.Ticker("BTC-USD").info
# for key, val in info.items():
#     print(key, " : ", val)