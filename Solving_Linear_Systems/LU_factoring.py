import numpy as np

np.set_printoptions(suppress=True)

def get_lu(A, b):
    n = len(A)
    O = np.copy(A)
    L = np.eye(n)
    
    for i in range(n-1):
        j = i+1

        # swapping
        if A[i,i] == 0:
            k = i+1
            swapped = False

            while k < n:
                if A[k, i] != 0:
                    # swaps 'A's values
                    temp = np.copy(A[i,:])
                    A[i,:] = A[k,:]
                    A[k,:] = temp

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
            multiplier = A[j, i] / A[i, i]
            L[j,i] = multiplier

            A[j, :] = (multiplier * A[i, :]) - A[j, :]
            b[j] = (multiplier * b[i]) - b[j]

            j = j+1
            
    print("Original Matrix\n{2}\nMatrix L\n{0}\nMatrix U\n{1}\n\n".format(L, A, O))
    print(np.dot(L,A))
    print("Matrices are equal? {0}".format(np.allclose(np.dot(L, A), O)))


A = np.array([[4.,-2.,2.],[-2.,10.,-7.],[2.,-7.,30.]])
b = np.array([6.,-3.,78.])

get_lu(A,b)
