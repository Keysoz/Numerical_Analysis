import numpy as np
import sys
n = 3
a = np.zeros((n, n + 1))
x = np.zeros(n)
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))
print(a)
# Applying Gauss Elimination with partial pivoting
z=0
for P in range(z + 2, n):
    if abs(a[z, z]) < abs(a[P, z]):
        a[[P, z]] = a[[z, P]]
for P in range(z, n):
    if abs(a[z, z]) < abs(a[P, z]):
        a[[P, z]] = a[[z, P]]
print(a)

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]
print(a)
# Back Substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]
print('x0 = %0.2f , x1 = %0.2f , x2 = %0.2f'%(x[0],x[1],x[2]))