from pandas import Series
from statsmodels.tsa.stattools import adfuller
from numpy import log
print "pre whitening of HUMIDITY"
series = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_humid.csv', header=0)
X = series.values
X = log(X)
result = adfuller(X)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
print " pre whitening of PRECIPITATION"
series1 = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_precip.csv', header=0)
X1 = series1.values
X1 = log(X1)
result1 = adfuller(X1)
print('ADF Statistic: %f' % result1[0])
print('p-value: %f' % result1[1])
for key, value in result1[4].items():
	print('\t%s: %.3f' % (key, value))
