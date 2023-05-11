import numpy as np
def gu(fu):
    poly = np.poly1d(fu)
    return poly
def f(x):
    poly = gu(fu)
    cul = poly(x)
    return cul
def false_position(xl, xu, e):
    step = 1
    print('\n\n** FALSE POSITION METHOD IMPLEMENTATION **')
    condition = True
    old=0
    xr=0
    fristIteration = True
    while condition:
        old=xr
        xr = xu - ((xl - xu) * f(xu) / (f(xl) - f(xu)))
        if  fristIteration == True:
            l = 0
            print('Iteration %d, xl = %0.6f and f(xl) = %0.6f,xu = %0.6f and f(xu) = %0.6f,xr = %0.6f and f(xr) = %0.6f  , error =%.6f'%(step,xl,f(xl),xu,f(xu),xr,f((xr)),l),"%")
            fristIteration =False

        else:
            l = abs((xr - old) / xr) * 100
            print('Iteration %d, xl = %0.6f and f(xl) = %0.6f,xu = %0.6f and f(xu) = %0.6f,xr = %0.6f and f(xr) = %0.6f  , error =%.6f'%(step,xl,f(xl),xu,f(xu),xr,f((xr)),l),"%")
        condition = abs(((xr - old) / xr) * 100) >= e
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        step = step + 1

    print('\nRequired Root is : %0.8f' % xr)
g = 0
i = int(input("Please Enter The Max Of Pow X="))
fu = [0]
step2 = i
while g <= i:

    z = float(input('Please Enter The Number Before X^%d Variable='%(step2)))
    fu.append(z)
    g = g + 1
    step2=step2-1
gu(fu)
xl = float(input('XL:= '))
xu = float(input('XU:= '))
e = float(input("Tolerable Error %:= "))
print(np.poly1d(fu))
if f(xl) * f(xu) < 0.0:
    false_position(xl, xu, e)

else:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
