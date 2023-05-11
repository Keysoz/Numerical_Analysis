from sympy  import *
import numpy as np
def gu(fu):
    poly = np.poly1d(fu)
    return poly
def f(x):
    poly = gu(fu)
    cul = poly(x)
    return cul
def der(fu):
    poly = np.poly1d(fu)
    poly=poly.deriv()
    return poly
def gi(x):
   poly=der(fu)
   cul = poly(x)
   #print(cul )
   return cul
# Implementing Newton Raphson Method
def newtonRaphson(xl, e):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    old=0
    xr=0
    fristIteration = True
    condition = True
    while condition:
        old = xr
        if gi(xl) == 0:
            print('Divide by zero error!')
            break
        xr = xl - (f(xl) / gi(xl))
        if fristIteration == True:
            l=0
            print('Iteration %d,xl = %0.6f and f(xl) = %0.6f,f`(xl) = %0.6f ,x1 = %0.6f and f(x1) = %0.6f, error =%.6f' % (step, xl, f(xl), gi(xl), xr, f(xr), l), "%")
            fristIteration = False
        else:
            l = abs((xr - old) / xr) * 100
            print('Iteration %d,xl = %0.6f and f(xl) = %0.6f,f`(xl) = %0.6f ,x1 = %0.6f and f(x1) = %0.6f, error =%.6f' % (step, xl, f(xl), gi(xl), xr, f(xr), l), "%")
        condition = abs(((xr - old) / xr) * 100) >= e
        xl = xr
        step = step + 1
    if condition == False:
        print('\nRequired root is: xr= %0.8f' % xr)
    else:
        print('\nNot Convergent.')

g = 0
i = int(input("Please Enter the max of pow X="))
fu = [0]
step2 = i
while g <= i:

    z = float(input('Please Enter The Number Before X^%d Variable='%(step2)))
    fu.append(z)
    g = g + 1
    step2=step2-1
gu(fu)
# Input Section
xl = float(input('Enter Guess: '))
e = float(input("Tolerable Error %:= "))
print(np.poly1d(fu))
newtonRaphson(xl,e)