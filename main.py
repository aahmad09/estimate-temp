import pandas
import numpy

#an adjacency matrix to emulate a 2d grid of given size
def make_adjMat(size):
    n = size * size
    M = numpy.zeros(shape=(n, n))
    for r in range(size):
        for c in range(size):
            i = r * size + c
            if c > 0:
                M[i - 1, i] = M[i, i - 1] = 1
            if r > 0:
                M[i - size, i] = M[i, i - size] = 1
    return M


def make_edgeMat(top, right, bottom, left, n):
    b = numpy.zeros(shape=(n * n))
    for i in range(n * n):
        if i < n:
            b[i] += top
        if i % n == (n - 1):
            b[i] += right
        if i >= n * (n - 1):
            b[i] += bottom
        if i % n == 0:
            b[i] += left
    return b


if __name__ == "__main__":
    # input entries
    n = int(input("Enter n for an n by n grid: "))  # n by n matrix
    top = int(input("Enter top: "))  # T_top
    right = int(input("Enter right: "))  # T_right
    bottom = int(input("Enter bottom: "))  # T_bottom
    left = int(input("Enter left: "))  # T_left

    ###
    # Solving 4x = Cx+B, where2
    # x is the vector of equilibrium temperatures at grid points
    # C is the adjacency matrix of grid points
    # B is the vector of equilibrium temperatures at edges
    #
    # write 4x = Cx+B in the form Ax = B where A=4I-C
    # solve x= A^-1 B
    ###
    adj_mat = make_adjMat(n)  # make adjacency matrix
    c = numpy.dot(numpy.identity(n * n), 4)

    a = numpy.subtract(c, adj_mat)

    b = make_edgeMat(top, right, bottom, left, n)
    x = numpy.linalg.solve(a,b)
    x_table = numpy.split(x,n)
    
    middle_element = x_table[int(len(x_table)/2)][int(len(x_table)/2)]
    print("Temperature at each grid point presented as a table . . .")
    print(pandas.DataFrame(x_table, columns=list(range(1, n + 1)), index=list(range(1, n + 1))))
    print("*"*80)
    print(f"Temperature of the center grid point: {middle_element}")