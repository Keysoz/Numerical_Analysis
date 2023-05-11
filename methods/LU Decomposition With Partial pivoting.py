import pprint
import numpy
import numpy as np
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
n = 3
A = np.zeros((n, n + 1))
x = np.zeros(n)
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        A[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))
print(A)
z=0
for P in range(z + 2, n):
    if abs(A[z, z]) < abs(A[P, z]):
        A[[P, z]] = A[[z, P]]
P, L, U = scipy.linalg.lu(A)
print ("A:")
pprint.pprint(A)
print ("P:")
pprint.pprint(P)
print ("L:")
pprint.pprint(L)
print ("U:")
pprint.pprint(U)
x[n - 1] = U[n - 1][n] / U[n - 1][n - 1]
for i in range(n-2,-1,-1):
    x[i] = U[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - U[i][j] * x[j]
    x[i] = x[i] / U[i][i]
print('x0 = %0.2f , x1 = %0.2f , x2 = %0.2f'%(x[0],x[1],x[2]))

