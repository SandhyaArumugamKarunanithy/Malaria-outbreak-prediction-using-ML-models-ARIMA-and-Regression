import warnings
import itertools
import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')# data = sm.datasets.co2.load_pandas()
series = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_precip.csv', header = 0)# y = data.data
sarray=series.as_matrix(columns=None)
sa = sarray.reshape((1150,1))
series1 = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_mean_temp1.csv', header = 0)# y = data.data
sarray1=series1.as_matrix(columns=None)
sa1 = sarray1.reshape((1150,1))
series2 = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_humid.csv', header = 0)# y = data.data
sarray2=series2.as_matrix(columns=None)
sa2 = sarray2.reshape((1150,1))
arr=[]
#print series
#series.plot(figsize = (15, 6))
#plt.show()
for i in range(0, 1150, 25):
	AIC_list=None
	AIC_list1=None
	AIC_list2=None
	# Define the p, d and q parameters to take any value between 0 and 2
	p = d = q = range(0, 2)

	# Generate all different combinations of p, q and q triplets
	pdq = list(itertools.product(p, d, q))

	# Generate all different combinations of seasonal p, q and q triplets
	seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

	print('Examples of parameter combinations for Seasonal ARIMA...')
	print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
	print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
	print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
	print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
	warnings.filterwarnings("ignore") # specify to ignore warning messages
	AIC_list = pd.DataFrame({}, columns=['param','param_seasonal','AIC'])
	AIC_list1 = pd.DataFrame({}, columns=['param','param_seasonal','AIC'])
	AIC_list2 = pd.DataFrame({}, columns=['param','param_seasonal','AIC'])
	for param in pdq:
		for param_seasonal in seasonal_pdq:
			try:
				mod = sm.tsa.statespace.SARIMAX(sa[0:25,-1],
												order=param,
												seasonal_order=param_seasonal,
												enforce_stationarity=False,
												enforce_invertibility=False)

				results = mod.fit()

				#print('ARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
				temp = pd.DataFrame([[ param ,  param_seasonal , results.aic ]], columns=['param','param_seasonal','AIC'])
				AIC_list = AIC_list.append( temp, ignore_index=True)
				del temp
				#print(AIC_list)
				
				mod = sm.tsa.statespace.SARIMAX(sa1[0:25,-1],
												order=param,
												seasonal_order=param_seasonal,
												enforce_stationarity=False,
												enforce_invertibility=False)

				results = mod.fit()

				#print('ARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
				temp = pd.DataFrame([[ param ,  param_seasonal , results.aic ]], columns=['param','param_seasonal','AIC'])
				AIC_list1 = AIC_list1.append( temp, ignore_index=True)
				del temp
				
				mod = sm.tsa.statespace.SARIMAX(sa2[0:25,-1],
												order=param,
												seasonal_order=param_seasonal,
												enforce_stationarity=False,
												enforce_invertibility=False)

				results = mod.fit()

				#print('ARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
				temp = pd.DataFrame([[ param ,  param_seasonal , results.aic ]], columns=['param','param_seasonal','AIC'])
				AIC_list2 = AIC_list2.append( temp, ignore_index=True)
				del temp
			except:
				print('error')
				continue
	print(AIC_list)
	m = np.amin(AIC_list['AIC'].values) # Find minimum value in AIC
	l = AIC_list['AIC'].tolist().index(m) # Find index number for lowest AIC
	Min_AIC_list = AIC_list.iloc[l,:]

	print(AIC_list1)
	m = np.amin(AIC_list1['AIC'].values) # Find minimum value in AIC
	l = AIC_list1['AIC'].tolist().index(m) # Find index number for lowest AIC
	Min_AIC_list1 = AIC_list1.iloc[l,:]

	print(AIC_list2)
	m = np.amin(AIC_list2['AIC'].values) # Find minimum value in AIC
	l = AIC_list2['AIC'].tolist().index(m) # Find index number for lowest AIC
	Min_AIC_list2 = AIC_list2.iloc[l,:]

	mod = sm.tsa.statespace.SARIMAX(sa[0:25,-1],
									order=Min_AIC_list['param'],
									seasonal_order=Min_AIC_list['param_seasonal'],
									enforce_stationarity=False,
									enforce_invertibility=False)
	results = mod.fit()

	print("### Min_AIC_list for precipitation### \n{}".format(Min_AIC_list))

	mod = sm.tsa.statespace.SARIMAX(sa1[0:25,-1],
									order=Min_AIC_list1['param'],
									seasonal_order=Min_AIC_list1['param_seasonal'],
									enforce_stationarity=False,
									enforce_invertibility=False)
	results1 = mod.fit()

	print("### Min_AIC_list for temperature### \n{}".format(Min_AIC_list1))

	mod = sm.tsa.statespace.SARIMAX(sa2[0:25,-1],
									order=Min_AIC_list2['param'],
									seasonal_order=Min_AIC_list2['param_seasonal'],
									enforce_stationarity=False,
									enforce_invertibility=False)
	results2 = mod.fit()

	print("### Min_AIC_list for humidity### \n{}".format(Min_AIC_list2))

	print(results.summary().tables[1])
	residuals = DataFrame(results.resid)
	residuals.plot()
	plt.title('precipitation')
	#plt.show()
	#residuals.plot(kind='kde')
	#plt.show()
	#plot_pacf(residuals, lags=100)
	#results.plot_diagnostics(figsize=(15, 12))
	#plt.show()
	print(residuals.describe())

	print(results1.summary().tables[1])
	residuals = DataFrame(results1.resid)
	residuals.plot()
	plt.title('temperature')
	#plt.show()
	#residuals.plot(kind='kde')
	#plt.show()
	#plot_pacf(residuals, lags=100)
	#results.plot_diagnostics(figsize=(15, 12))
	#plt.show()
	print(residuals.describe())

	print(results2.summary().tables[1])
	residuals = DataFrame(results2.resid)
	residuals.plot()
	plt.title('Humidity')
	#plt.show()
	#residuals.plot(kind='kde')
	#plt.show()
	#plot_pacf(residuals, lags=100)
	#results.plot_diagnostics(figsize=(15, 12))
	#plt.show()
	print(residuals.describe())
	
	if(min(Min_AIC_list['AIC'], Min_AIC_list1['AIC'], Min_AIC_list2['AIC']) == Min_AIC_list['AIC']):
		arr.append('precip')
	elif(min(Min_AIC_list['AIC'], Min_AIC_list1['AIC'], Min_AIC_list2['AIC']) == Min_AIC_list1['AIC']):
		arr.append('temp')
	elif(min(Min_AIC_list['AIC'], Min_AIC_list1['AIC'], Min_AIC_list2['AIC']) == Min_AIC_list2['AIC']):
		arr.append('humid')
print arr
f=open('factor.py', 'w')
f.write('arr='+repr(arr))
f.close()