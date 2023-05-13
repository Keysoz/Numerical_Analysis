import numpy as np

def gu(fu):
    poly = np.poly1d(fu)
    return poly


def f(x):
    poly = gu(fu)
    cul = poly(x)
    return cul


def bisection(xl, xu, e):
    step = 1
    my_wrie_file = open('../files/bisection.txt', 'w')
    my_wrie_file.write('\n\n** BISECTION METHOD IMPLEMENTATION **\n--------------------------------------------------')
    my_wrie_file.close()
    condition = True
    old = 0
    xr = 0
    fristIteration = True
    fristIteration1 = True
    while condition:
        old = xr
        xr = (xl + xu) / 2

        if fristIteration == True:
            l = 0
            my_wrie_file = open('../files/bisection.txt', 'a')
            my_wrie_file.write(('Iteration %d, xl = %0.6f and f(xl) = %0.6f,xu = %0.6f and f(xu) = %0.6f,xr = %0.6f and f(xr) = %0.6f  , error =%.6f\n' % (
                step, xl, f(xl), xu, f(xu), xr, f(xr), l)))
            my_wrie_file.close()

            fristIteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_wrie_file = open('../files/bisection.txt', 'a')
            my_wrie_file.write((
                '\nIteration %d, xl = %0.6f and f(xl) = %0.6f,xu = %0.6f and f(xu) = %0.6f,xr = %0.6f and f(xr) = %0.6f  , error =%.6f\n' % (
                    step, xl, f(xl), xu, f(xu), xr, f(xr), l)))
            my_wrie_file.close()

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        step = step + 1
        if fristIteration1:
            condition = True
            fristIteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
    my_wrie_file = open('../files/bisection.txt', 'a')
    my_wrie_file.write('\nRequired Root is : %0.8f=' % xr)
    my_wrie_file.close()
g = 0
i = int(input("Please Enter The Max Of Pow X="))
fu = [0]
step2 = i
while g <= i:
    z = float(input('Please Enter The Number Before X^%d Variable=' % step2))
    fu.append(z)
    g = g + 1
    step2 = step2 - 1
xl = float(input('XL:= '))
xu = float(input('XU:= '))
e = float(input("Tolerable Error %:= "))
my_wrie_file = open('../files/bisection.txt', 'w')
my_wrie_file.write(str(np.poly1d(fu)))
my_wrie_file.close()
if f(xl) * f(xu) < 0.0:
    bisection(xl, xu, e)
else:
    my_wrie_file = open('../files/bisection.txt', 'w')
    my_wrie_file.write('Given guess values do not bracket the root.\nTry Again with different guess values.')
    my_wrie_file.close()

my_wrie_file = open('../files/bisection.txt', 'a')
my_wrie_file.write(str(i))
my_wrie_file.close()