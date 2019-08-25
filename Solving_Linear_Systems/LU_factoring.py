import numpy as np

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
    print(np.dot(L,U))
    print("Matrices are equal? {0}".format(np.allclose(np.dot(L, U), A)))


A = np.array([[2.,1.,0.,0.],[-1.,3.,3.,0.],[2.,-2.,1.,4.],[-2.,2.,2.,5.]])
b = np.array([2., 3., 4., 5.])

get_lu(A,b)
