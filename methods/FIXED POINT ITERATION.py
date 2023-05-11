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

        condition = abs(f(xr)) > e

    print('\nRequired root is: %0.8f' % xr)

gi = 0
i = int(input("Please Enter The Max Of Pow X="))
fu = [0]
step2 = i
while gi <= i:
    z = float(input('Please Enter The Number Before X^%d Variable='%(step2)))
    fu.append(z)
    gi = gi + 1
    step2=step2-1
gu(fu)
xl = float(input('xl= '))
e = float(input("Tolerable Error %:= "))
fixedPointIteration(xl, e)