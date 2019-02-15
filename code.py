import pandas as p
import numpy as n

a = p.read_csv('fulldata.csv');
b = a[['Close']] # taking only the closing values
b = n.ravel(b) # converting into 1d array
w = n.repeat(0.1,10) # the value is set to 0.1 because we are mean with window 10
r_avg = n.convolve(b,w,'valid')
print(r_avg)
