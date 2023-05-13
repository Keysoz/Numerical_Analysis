import numpy as np
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
def lu_method(items_list):
    n = 3
    A = np.zeros((n, n + 1))
    x = np.zeros(n)
    for i in range(n):
        for j in range(n + 1):
            A[i][j] = items_list[i][j]
    P, L, U = scipy.linalg.lu(A)
    my_write_file = open('files/lu_1.txt', 'w')
    my_write_file.write("A:\n")
    for y in A:
        my_write_file.write("           ")
        for h in y:
            my_write_file.write(str(round(h, 2)) + "        ")
        my_write_file.write("\n")
    my_write_file.write("\n\n\n\n")
    my_write_file.close()

    my_write_file = open('files/lu_1.txt', 'a')
    my_write_file.write("L:\n")
    for y in L:
        my_write_file.write("           ")
        for h in y:
            my_write_file.write(str(round(h, 2)) + "        ")
        my_write_file.write("\n")
    my_write_file.write("\n\n\n\n")
    my_write_file.close()

    my_write_file = open('files/lu_2.txt', 'w')
    my_write_file.write("U:\n")
    for y in U:
        my_write_file.write("           ")
        for h in y:
            my_write_file.write(str(round(h, 2)) + "        ")
        my_write_file.write("\n")
    my_write_file.close()
    x[n - 1] = U[n - 1][n] / U[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = U[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - U[i][j] * x[j]
        x[i] = x[i] / U[i][i]
    my_write_file = open('files/lu_3.txt', 'w')
    my_write_file.write(
        str('\n\n           x1 = %0.2f , x2 = %0.2f , x3 = %0.2f' % (x[0], x[1], x[2])))
    my_write_file.close()
my_list = [[7, 8, 5, 6], [4, 6, 7, 8], [5, 6, 7, 8]]
lu_method(my_list)
