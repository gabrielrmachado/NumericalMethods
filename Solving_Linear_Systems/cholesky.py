import numpy as np
import math
from scipy.linalg import solve_triangular

def cholesky_factorization(A):
    n = len(A)
    L = np.eye(n)
    
    for i in range(n):
        for j in range(n):
            
            if j > i:
                continue
            
            # check if the element belongs to the main diagonal
            if i == j:
                L[i,i] = math.sqrt(A[i,i] - np.sum(np.square(L[i,:j])))
            else:
                s = 0
                for k in range(j):
                    s = s + (L[i,k] * L[j,k])
                    
                L[i,j] = (A[i,j] - s) / L[j,j]
    
    Lt = np.transpose(L)
    print("Matrix 'L'\n{0}\nMatrix 'Lt'\n{1}".format(L, Lt))
    print("\n'L' x 'Lt' = 'A'? {0}".format(np.allclose(np.dot(L, Lt), A)))

    return L, Lt

def LU_solve(L, U, b):
    y = solve_triangular(L, b, lower=True)
    x = solve_triangular(U, y)
    sol = np.linalg.solve(np.dot(L,U), b)

    print("\nSolution 'x': {0}".format(x))
    print("Solution 'x' NUMPY: {0}".format(sol))

    print("Solutions are the same? {0}".format(np.allclose(sol, x)))
    return x
    
A = np.array([[4.,-2.,2.],[-2.,10.,-7.],[2.,-7.,30.]])
L, Lt = cholesky_factorization(A)
b = [6.,-3.,78.]

x = LU_solve(L, Lt, b)