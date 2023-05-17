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
def fixed_point(xl, e):
    step = 1

    my_write_file = open('methods/fixed_point.txt', 'a')
    my_write_file.write(
        '\n\n** Fixed Point METHOD IMPLEMENTATION **\n--------------------------------------------------\n')
    my_write_file.close()
    condition = True
    old = 0
    xr = 0
    first_iteration = True
    first_iteration1 = True
    while condition:
        old = xr
        xr = g(xl)

        if first_iteration:
            l = 0
            my_write_file = open('methods/fixed_point.txt', 'a')
            my_write_file.write((
                    'Iteration %d | xl = %0.6f | f(xl) = %0.6f | '
                    'xr = %0.6f | f(xr) = %0.6f | error =%.2f    ‰ \n' % (
                        step, xl, f(xl), xr, f(xr), l)))
            my_write_file.close()

            first_iteration = False
        else:
            l = abs((xr - old) / xr) * 100
            my_write_file = open('methods/fixed_point.txt', 'a')
            my_write_file.write((
                    'Iteration %d | xl = %0.6f | f(xl) = %0.6f | '
                    'xr = %0.6f | f(xr) = %0.6f | error =%.2f    ‰ \n' % (
                        step, xl, f(xl), xr, f(xr), l)))
            my_write_file.close()

        xl = xr
        step = step + 1
        if first_iteration1:
            condition = True
            first_iteration1 = False
        else:
            condition = abs(((xr - old) / xr) * 100) >= e
        condition = abs(f(xr)) > e
    my_write_file = open('methods/fixed_point.txt', 'a')
    my_write_file.write('\nRequired Root is : %0.8f=' % xr)
    my_write_file.close()
gi = 0
i = int(input("Please Enter The Max Of Pow X="))
fu = [0]
step2 = i
while gi <= i:
    z = float(input('Please Enter The Number Before X^%d Variable=' % step2))
    fu.append(z)
    gi = gi + 1
    step2=step2-1
gu(fu)
xl = float(input('xl= '))
e = float(input("Tolerable Error %:= "))
fixed_point(xl, e)