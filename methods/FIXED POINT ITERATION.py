import numpy as np
import math
def gu(fu):
    poly = np.poly1d(fu)
    return poly
def f(x):
    poly = gu(fu)
    cul = poly(x)
    return cul
def g(x):
    return 1 / math.sqrt(1 + x)
# Implementing Fixed Point Iteration Method
def fixedPointIteration(xl, e):
    xr=0
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    old = 0
    condition = True
    fristIteration = True
    fristIteration1 = True
    while condition:
        old=xr
        xr = g(xl)
        if  fristIteration == True:
            l=0
            print('Iteration-%d, xr = %0.6f and f(xr) = %0.6f  and error %0.6f' % (step, xr, f(xr),l),"%")
            fristIteration = False
        else:
            l= abs(xr-old)/xr*100
            print('Iteration-%d, xr = %0.6f and f(xr) = %0.6f  and error %0.6f' % (step, xr, f(xr), l),"%")
        xl = xr
        step = step + 1
        if fristIteration1 == True:
            condition = True
            fristIteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
    print('\nRequired Root is : %0.8f=' % xr)
fu = [-0.9, 1.7, 2.5]
xl = 5
e = 0.7
fixedPointIteration(xl, e)