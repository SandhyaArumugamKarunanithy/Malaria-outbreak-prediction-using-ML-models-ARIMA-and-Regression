from factor import arr
from random import seed
from random import randrange
from sklearn import metrics
from csv import reader
from math import sqrt
import csv
from csv import DictReader
import matplotlib.pyplot as plt
import array
import numpy as np
# Load a CSV file
def load_csv('C:\Users\Karunanithi\Downloads\fin\afg_deaths.csv'):
	dataset = list()
	with open(filename, 'rU') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy
 
# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)
 
# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split, *args):
	if(arr[country]=='precip'):
		x = [row[0] for row in dataset]
		y = [row[3] for row in dataset]
	elif(arr[country]=='temp'):
		x = [row[1] for row in dataset]
		y = [row[3] for row in dataset]
	elif(arr[country]=='humid'):
		x = [row[2] for row in dataset]
		y = [row[3] for row in dataset]
	sub=[]
	for i in range(25):
		sub.append([])
		sub[i].append(x[i])
		sub[i].append(y[i])
	print sub
	train, test = train_test_split(sub, split)
	test_set = list()
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(train, test_set, *args)
	actual = [row[-1] for row in test]
	
	a = array.array('i',(i for i in range(0,len(actual))))
	#print a
	print "actual:"
	print actual
	rmse = rmse_metric(actual, predicted)
	ae = metrics.mean_absolute_error(actual, predicted)
	plt.plot(a,actual)
	plt.plot(a,predicted)
	plt.legend(['actual', 'predicted'], loc='upper left')
	pmean = mean(predicted)
	pred_mean.append(pmean)
	#plt.show()
	ae_arr.append(ae)
	return rmse
 
# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))
 
# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar
 
# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])
 
# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]
 
# Simple linear regression algorithm
def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	#print predictions
	return predictions
 

seed(1)
# load and prepare data	
filename = 'C:\\Users\\user\\Desktop\\FYP\\afg_lr.csv'
rmse_arr=[]
pred_mean=[]
ae_arr = []
country=0
pmean = 0
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
for i in range(0, 1150, 25):
	#print dataset[i:i+25]
	# evaluate algorithm
    split = 0.6
    rmse = evaluate_algorithm(dataset[i:i+25], simple_linear_regression, split)
    print('RMSE: %.3f' % (rmse))
    rmse_arr.append(rmse)
    country=country+1
print "RMSE:"
print rmse_arr
#print pred_mean
f=open('factor1.py', 'w')
f.write('pred_mean='+repr(pred_mean))
f.close()
print "Mean Absolute Error:"
print ae_arr