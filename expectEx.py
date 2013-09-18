#!/usr/bin/python

import numpy

# function to calulate covariance 
# E(XY) - E(X) * E(Y)
def getCov(x, y):
    xymean = 0
    for i in range (len(x)):
        xymean += x[i] * y[i]
    xymean /= len(x)
    covari = xymean - numpy.mean(x) * numpy.mean(y)
    return covari


x = [12.0, 11.0, 2.5, 20.9]
y = [6.0, 3.0, 1.0, 4.2]

myCov = getCov(x, y)
print x
print y
print "Covariance(x,y): ", myCov, "\n\n"


