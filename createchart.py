import pandas as pd
import datetime as dt
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt

x = int(input('start year: '))
y = int(input('start month: '))
z = int(input('start day: '))

a = int(input('end year: '))
b = int(input('end month: '))
c  =int(input('end day: '))

start = dt.date(x,y,z)
end = dt.date(a,b,c)

code1 = input('get_code1: ') + '.JP'
code2 = input('get_code2: ') + '.JP'

df1 = data.DataReader(code1,'stooq',start,end)
df2 = data.DataReader(code2,'stooq',start,end)


df = pd.DataFrame({code1:df1['Close'], code2:df2['Close']})
df.plot(grid=True)
plt.show()