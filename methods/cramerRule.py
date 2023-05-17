import numpy as np
import scipy
import scipy.linalg  # SciPy Linear Algebra Library
# determinant of Matrix
def determinantOfMatrix(mat):
    ans = (mat[0][0] * (mat[1][1] * mat[2][2] -
                        mat[2][1] * mat[1][2]) -
           mat[0][1] * (mat[1][0] * mat[2][2] -
                        mat[1][2] * mat[2][0]) +
           mat[0][2] * (mat[1][0] * mat[2][1] -
                        mat[1][1] * mat[2][0]))
    return ans


# This function finds the solution of system of
# linear equations using cramer's rule
def findSolution(coeff):
    # Matrix d using coeff as given in
    # cramer's rule
    d = [[coeff[0][0], coeff[0][1], coeff[0][2]],
         [coeff[1][0], coeff[1][1], coeff[1][2]],
         [coeff[2][0], coeff[2][1], coeff[2][2]]]

    # Matrix d1 using coeff as given in
    # cramer's rule
    d1 = [[coeff[0][3], coeff[0][1], coeff[0][2]],
          [coeff[1][3], coeff[1][1], coeff[1][2]],
          [coeff[2][3], coeff[2][1], coeff[2][2]]]

    # Matrix d2 using coeff as given in
    # cramer's rule
    d2 = [[coeff[0][0], coeff[0][3], coeff[0][2]],
          [coeff[1][0], coeff[1][3], coeff[1][2]],
          [coeff[2][0], coeff[2][3], coeff[2][2]]]

    # Matrix d3 using coeff as given in
    # cramer's rule
    d3 = [[coeff[0][0], coeff[0][1], coeff[0][3]],
          [coeff[1][0], coeff[1][1], coeff[1][3]],
          [coeff[2][0], coeff[2][1], coeff[2][3]]]

    # Calculating Determinant of Matrices
    # d, d1, d2, d3
    D = determinantOfMatrix(d)
    D1 = determinantOfMatrix(d1)
    D2 = determinantOfMatrix(d2)
    D3 = determinantOfMatrix(d3)

    my_write_file = open('files/cramer_2.txt', 'w')
    my_write_file.write(f"\n      D is : " + str(D) + "\n")
    my_write_file.close()
    my_write_file = open('files/cramer_2.txt', 'a')
    my_write_file.write(f"      D1 is : " + str(D1) + "\n")
    my_write_file.write(f"      D2 is : " + str(D2) + "\n")
    my_write_file.write(f"      D3 is : " + str(D3) + "\n")
    my_write_file.close()

    # Case 1
    if (D != 0):

        # Coeff have a unique solution.
        # Apply Cramer's Rule
        x = D1 / D
        y = D2 / D

        # calculating z using cramer's rule
        z = D3 / D
        my_write_file = open('files/cramer_3.txt', 'w')
        my_write_file.write("\n       Value of x is : " + str(x) + "\n")
        my_write_file.close()
        my_write_file = open('files/cramer_3.txt', 'a')
        my_write_file.write("       Value of y is : " + str(y) + "\n")
        my_write_file.write("       Value of z is : " + str(z) + "\n")
        my_write_file.close()

    # Case 2
    else:
        if (D1 == 0 and D2 == 0 and
                D3 == 0):
            my_write_file = open('files/cramer_3.txt', 'w')
            my_write_file.write("\n\n\n\t\t\tInfinite solutions")
            my_write_file.close()
        elif (D1 != 0 or D2 != 0 or
              D3 != 0):
            my_write_file = open('files/cramer_3.txt', 'w')
            my_write_file.write("\n\n\n\t\t\tNo solutions")
            my_write_file.close()


# Driver Code
def cramer(items_list):
    # storing coefficients of linear
    # equations in coeff matrix


    n = 3
    coeff= np.zeros((n, n + 1))
    x = np.zeros(n)
    for i in range(n):
        for j in range(n + 1):
            coeff[i][j] = items_list[i][j]
    my_write_file = open('files/cramer_1.txt', 'w')
    for y in coeff:
        my_write_file.write("\n     ")
        for h in y:
            my_write_file.write(str(h) + "        ")
    my_write_file.close()
    findSolution(coeff)