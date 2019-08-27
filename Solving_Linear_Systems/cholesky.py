import numpy as np
import math

def cholesky_factorization(A):
    n = len(A)
    L = np.eye(n)
    
    # initial conditions
    # L[0,0] = math.sqrt(A[0,0])
    # L[1,0] = A[1,0] / L[0,0]
    
    for i in range(n):
        for j in range(n):
            
            if j > i:
                continue
            
            # check if the element is in the main diagonal
            if i == j:
                L[i,i] = math.sqrt(A[i,i] - np.sum(np.square(L[i,:j])))
            else:
                s = 0
                for k in range(j):
                    s = s + (L[i,k]*L[j,k])
                    
                L[i,j] = (A[i,j] - s) / L[j,j]
    
    Lt = np.transpose(L)
    print("Matrix 'L'\n{0}\nMatrix 'Lt'\n{1}".format(L, Lt))
    print("'L' x 'Lt' = 'A'? {0}".format(np.allclose(np.dot(L, Lt), A)))
    
A = np.array([[4.,-2.,2.],[-2.,10.,-7.],[2.,-7.,30.]])
cholesky_factorization(A)
