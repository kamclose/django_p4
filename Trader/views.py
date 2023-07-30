from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
import yfinance as yf
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import io 
import base64

# Create your views here.
def home(request):
    search_query = request.GET.get('search_query', 'BTC-USD')

    data = yf.download(search_query, "2017-01-01") 
    try:
        dates = mdates.date2num(data.index.to_pydatetime())
        plt.plot_date(dates, data['Adj Close'], '-')

        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
        plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())

        plt.grid(True)
        plt.ylabel(r'Price [$]')
        plt.title(f'{search_query} Price')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
        for label in plt.gca().get_xticklabels(which='major'):
            label.set(rotation=30, horizontalalignment='right')

        buf = io.BytesIO() 
        plt.savefig(buf, format='png')
        buf.seek(0)

        data_uri = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
    except:
        data_uri = None

    return render(request, 'index.html', {'data_uri': data_uri})