import numpy as np
from colors import bcolors
from matrix_utility import swap_row

def gaussianElimination(mat):
    N = len(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:
        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    return backward_substitution(mat)

def forward_substitution(mat):
    N = len(mat)
    for k in range(N):

        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > abs(v_max):
                v_max = mat[i][k]
                pivot_row = i

        if mat[pivot_row][k] == 0:
            return k  # Matrix is singular

        if pivot_row != k:
            swap_row(mat, k, pivot_row)

        for i in range(k + 1, N):
            m = mat[i][k] / mat[k][k]
            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * m
            mat[i][k] = 0

    return -1

def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)

    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N]
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]

    return x

if __name__ == '__main__':
    A_b = [
        [10,  8,   1,  -7],
        [ 4, 10,  -5,   2],
        [ 5,  1,  10, 1.5]
    ]

    result = gaussianElimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
