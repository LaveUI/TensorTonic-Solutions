import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    if not A or not A[0]:
        return []

    row = len(A)
    col = len(A[0])
    t = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            t[j][i] = A[i][j]

    return np.array(t)
    pass
