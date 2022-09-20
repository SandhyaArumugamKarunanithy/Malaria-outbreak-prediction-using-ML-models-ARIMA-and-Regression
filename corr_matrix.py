import numpy as np
import pandas as pd
from pandas import Series
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf
from pandas.plotting import autocorrelation_plot
series = pd.read_csv('C:\Users\Karunanithi\Desktop\FYP\afg_corr.py', header=0)
df = pd.DataFrame(series)
temp=[]
humid=[]
prec=[]
#print df.iloc[0:10, 0]
for i in range(0,1150,25):
	temp.append(df.iloc[i:i+25, 3].corr(df.iloc[i:i+25, 1]))
	humid.append(df.iloc[i:i+25, 3].corr(df.iloc[i:i+25, 2]))
	prec.append(df.iloc[i:i+25, 3].corr(df.iloc[i:i+25, 0]))
#print(df.corr())
#logv=np.log(df['All ages'])
#print logv
print("Correlation between malaria incidence and temperature for all African countries:")
print temp
print("Correlation between malaria incidence and humidity for all African countries:")
print humid
print("Correlation between malaria incidence and precipitation for all African countries:")
print prec