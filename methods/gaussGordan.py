# Importing NumPy Library
import numpy as np
def gauss_gordan(items_list):
    n = 3
    # Making numpy array of n x n+1 size and initializing
    # to zero for storing augmented matrix
    a = np.zeros((n, n + 1))
    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    x = np.zeros(n)
    # Reading augmented matrix coefficients
    for i in range(n):
        for j in range(n + 1):
            a[i][j] = items_list[i][j]
    # Applying Gauss Jordan Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            my_write_file = open('files/gordan_1.txt', 'w')
            my_write_file.write("\n\n\n\tDivide by zero detected!\n")
            my_write_file.close()
        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]

                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    my_write_file = open('files/gordan_1.txt', 'w')
    for y in a:
        my_write_file.write("\n                        ")
        for h in y:
            my_write_file.write(str(round(h, 2)) + "        ")
    my_write_file.write("\n")
    my_write_file.close()
    # Obtaining Solution
    for i in range(n):
        x[i] = a[i][n] / a[i][i]
    # Displaying solution
    my_write_file = open('files/gordan_2.txt', 'w')
    my_write_file.write('\n')
    my_write_file.write('\n')
    my_write_file.close()
    for i in range(n):
        my_write_file = open('files/gordan_2.txt', 'a')
        my_write_file.write('           X%d = %0.2f            ' % (i, x[i]))
        my_write_file.close()