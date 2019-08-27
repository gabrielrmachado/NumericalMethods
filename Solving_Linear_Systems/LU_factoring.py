import numpy as np
from scipy.linalg import solve_triangular

np.set_printoptions(suppress=True)

def get_lu(A, b):
    n = len(A)
    U = np.copy(A)
    L = np.eye(n)
    
    for i in range(n-1):
        j = i+1

        # swapping
        if U[i,i] == 0:
            k = i+1
            swapped = False

            while k < n:
                if U[k, i] != 0:
                    # swaps 'A's values
                    temp = np.copy(U[i,:])
                    U[i,:] = U[k,:]
                    U[k,:] = temp

                    # swaps 'b's values
                    temp = np.copy(b[i])
                    b[i] = b[k]
                    b[k] = temp

                    swapped = True
                    break

                else:
                    k = k+1
            
            if swapped == False:
                raise ValueError("No unique solutions")

        # elimination process
        while j < n:
            multiplier = U[j, i] / U[i, i]
            L[j,i] = multiplier

            U[j, :] = (-multiplier * U[i, :]) + U[j, :]
            b[j] = (-multiplier * b[i]) + b[j]

            j = j+1
            
    print("Original Matrix\n{2}\nMatrix L\n{0}\nMatrix U\n{1}\n\n".format(L, U, A))
    Ap = np.dot(L,U)
    print("{0}\nA = L x U? {1}".format(Ap, np.allclose(Ap, A)))

    return L, U, b

def LU_solve(L, U, b):
    y = solve_triangular(L, b, lower=True)
    x = solve_triangular(U, y)
    sol = np.linalg.solve(np.dot(L,U), b)

    print("\nSolution 'x': {0}".format(x))
    print("Solution 'x' NUMPY: {0}".format(sol))

    print("Solutions are the same? {0}".format(np.allclose(sol, x)))
    return x

A = np.array([[4.,-1.,1.],[-1.,4.25,2.75],[1.,2.75,3.5]])
b = np.array(np.zeros(A.shape[0]))

L, U, _ = get_lu(A,b)

b = np.array([1.,1.,-3.])
LU_solve(L, U, b)

b = np.array([8.,7.,14.])
LU_solve(L, U, b)




