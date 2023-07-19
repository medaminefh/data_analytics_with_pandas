import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_excel('base.xlsx', parse_dates=True, index_col=0)


df[['WTI', 'USDTND', 'TUNINDEX']].plot.line(subplots= True)

plt.show()