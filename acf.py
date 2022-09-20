from pandas import Series
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from pandas.plotting import autocorrelation_plot
series = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_precip.csv', header=0)
sarray=series.as_matrix(columns=None)
sa = sarray.reshape((1150,1))
#print sa[0:25,-1]
#print sa[25:50,-1]
#pyplot.title('hi')
for i in range(0, 1150, 25):
    print i
    print sa[i:i+25,-1]
    plot_acf(sa[i:i+25,-1], lags=10, title='ACF Plot for Preciptation Vs Lag')
    plot_pacf(sa[i:i+25,-1], lags=10, title='PACF Plot for Preciptation Vs Lag')
    pyplot.xlabel('LAG')
    pyplot.ylabel('CORRELATION')
    pyplot.show()

series = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_mean_temp1.csv', header=0)
sarray=series.as_matrix(columns=None)
sa = sarray.reshape((1150,1))
#print sa[0:25,-1]
#print sa[25:50,-1]
#pyplot.title('hi')
for i in range(0, 1150, 25):
    print i
    print sa[i:i+25,-1]
    plot_acf(sa[i:i+25,-1], lags=10, title='ACF Plot for Temperature Vs Lag')
    plot_pacf(sa[i:i+25,-1], lags=10, title='PACF Plot for Temperature Vs Lag')
    pyplot.xlabel('LAG')
    pyplot.ylabel('CORRELATION')
    pyplot.show()

series = Series.from_csv('C:\\Users\\user\\Desktop\\FYP\\afg_humid.csv', header=0)
sarray=series.as_matrix(columns=None)
sa = sarray.reshape((1150,1))
#print sa[0:25,-1]
#print sa[25:50,-1]
#pyplot.title('hi')
for i in range(0, 1150, 25):
    print i
    print sa[i:i+25,-1]
    plot_acf(sa[i:i+25,-1], lags=10, title='ACF Plot for Humidity Vs Lag')
    plot_pacf(sa[i:i+25,-1], lags=10, title='PACF Plot for Humidity Vs Lag')
    pyplot.xlabel('LAG')
    pyplot.ylabel('CORRELATION')
    pyplot.show()