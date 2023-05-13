import numpy as np
def gauss_partial(items_list):
    n = 3
    a = np.zeros((n, n + 1))
    x = np.zeros(n)
    for i in range(n):
        for j in range(n + 1):
            a[i][j] = items_list[i][j]
    my_write_file = open('files/gauss_partial_1.txt', 'w')
    for y in a:
        my_write_file.write("\n                        ")
        for h in y:
            my_write_file.write(str(h) + "        ")
    my_write_file.write("\n\n\n")
    my_write_file.close()
    # Applying Gauss Elimination with partial pivoting
    z=0
    for P in range(z + 1, n):
        if abs(a[z, z]) < abs(a[P, z]):
            a[[P, z]] = a[[z, P]]
    for P in range(z + 1, n):
        if abs(a[z + 1, z + 1]) < abs(a[P, z + 1]):
            a[[P, z + 1]] = a[[z + 1, P]]
    my_write_file = open('files/gauss_partial_1.txt', 'a')
    for y in a:
        my_write_file.write("                        ")
        for h in y:
            my_write_file.write(str(h) + "        ")
        my_write_file.write("\n")
    my_write_file.close()
    for i in range(n):
        if a[i][i] == 0.0:
            my_write_file = open('files/gauss_partial_1.txt', 'w')
            my_write_file.write("Divide by zero detected!")
            my_write_file.close()

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    # Back Substitution
    my_write_file = open('files/gauss_partial_2.txt', 'w')
    my_write_file.write(
        str('\n\n                                 x0 = %0.2f , x1 = %0.2f , x2 = %0.2f' % (x[0], x[1], x[2])))
    my_write_file.close()