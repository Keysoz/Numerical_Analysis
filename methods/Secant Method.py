import numpy as np
def gu(fu):
    poly = np.poly1d(fu)
    return poly
def f(x):
    poly = gu(fu)
    cul = poly(x)
    return cul

def secant(x0, x1, e):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    old = 0
    xr = 0
    fristIteration = True
    fristIteration1 = True
    while condition:
        old = xr
        xr = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        if fristIteration == True:
            l = 0
            print('Iteration %d, x0 = %0.6f and f(x0) = %0.6f,x1 = %0.6f and f(x1) = %0.6f,xr = %0.6f and f(xr) = %0.6f  , error =%.6f' % (step, x0, f(x0), x1, f(x1), xr, f((xr)), l), "%")
            fristIteration = False
        else:
            l = abs((xr - old) / xr) * 100
            print(
                'Iteration %d, xl = %0.6f and f(xl) = %0.6f,xu = %0.6f and f(xu) = %0.6f,xr = %0.6f and f(xr) = %0.6f  , error =%.6f' % (step, x0, f(x0), x1, f(x1), xr, f((xr)), l), "%")

        x0 = x1
        x1 = xr
        step = step + 1
        if fristIteration1 == True:
            condition = True
            fristIteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
    print('\n Required root is: %0.8f' % xr)



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
x0 = float(input('Enter First Guess X0:= '))
x1 = float(input('Enter Second Guess X1:= '))
e = float(input("Tolerable Error %:= "))
print(np.poly1d(fu))
secant(x0, x1, e)




