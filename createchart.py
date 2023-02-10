import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data

s_year = int(input('start year: '))
s_month = int(input('start month: '))
s_day = int(input('start day: '))

e_year = int(input('end year: '))
e_month = int(input('end month: '))
e_day  =int(input('end day: '))

start = dt.date(s_year, s_month, s_day)
end = dt.date(e_year, e_month, e_day)

code1 = input('get_code1: ') + '.JP'
code2 = input('get_code2: ') + '.JP'

stock_df1 = data.DataReader(code1,'stooq',start,end)
stock_df2 = data.DataReader(code2,'stooq',start,end)


df = pd.DataFrame({code1:stock_df1['Close'], code2:stock_df2['Close']})
df.plot(grid=True)
plt.show()