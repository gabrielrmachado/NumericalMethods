import numpy as np

np.set_printoptions(suppress=True)

def gaussian_np(A, b):
    x = np.linalg.solve(A, b)
    print("Solution 'x'\n{0}".format(x))


def gaussian(A, b):
    n = len(A)
    
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

            A[j, :] = (multiplier * A[i, :]) - A[j, :]
            b[j] = (multiplier * b[i]) - b[j]

            j = j+1
            
    print("Transformed system 'A'\n{0}".format(A))
    print("Transformed array 'b'\n{0}".format(b))

    # backward substitution
    k = n-1

    x = np.zeros(n)
    x[k] = b[k] / A[k,k]

    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:], x[k+1:])) / A[k,k]
        k = k-1
    
    print("Answer array 'x'\n{0}".format(x))

A = np.array([[1,1,0,1],[2,1,-1,1],[-1,2,3,-1],[3,-1,-1,2]])
b = np.array([2,1,4,-3])

print("NUMPY SOLUTION")
gaussian_np(A,b)
print("\nMY SOLUTION")
gaussian(A,b)