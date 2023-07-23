import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import dates as mlt_dates
""" plt.style.use('fivethirtyeight') """
df = pd.read_excel('base.xlsx', parse_dates=True, index_col=0)


df[['WTI', 'USDTND', 'TUNINDEX']].plot.line(subplots= True)

dates = mlt_dates.DateFormatter("%b, %d %Y")

series = df['TUNINDEX'].values
res = adfuller(series, autolag='AIC')

print('ADF Statistic: %f' % res[0])
print('p-value: %f' % res[1])

print('Critical values: ')

for key, value in res[4].items():
    print('\t%s: %.3f' % (key, value))


if (res[0] < res[4]['5%']):
    print('Reject Ho - Timeserie is stationary')
else:
    print('Failed to reject Ho - Timeserie is not stationary')


# plt.gca().xaxis.set_major_formatter(dates)

# plt.show()