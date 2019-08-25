import numpy as np

np.set_printoptions(suppress=True)

def gaussian_np(A, b):
    x = np.linalg.solve(A, b)
    print("Solution 'x'\n{0}".format(x))


def gaussian_partial(A, b):
    n = len(A)
    swapping = True
    
    for i in range(n-1):
        j = i+1

        # swapping
        maxColIndex = np.argmax(np.absolute(A[i:,i]))
        
        if A[maxColIndex+i,i] == 0:
            raise ValueError("No unique solutions")
        
        else:
            temp = np.copy(A[i,:])
            A[i,:] = A[maxColIndex+i,:]
            A[maxColIndex+i,:] = temp
            
            temp = np.copy(b[i])
            b[i] = b[maxColIndex+i]
            b[maxColIndex+i] = temp
            
            # print(A)
            # print(b)
            # print("\n")

        # elimination process
        while j < n:
            multiplier = A[j, i] / A[i, i]

            A[j, :] = (multiplier * A[i, :]) - A[j, :]
            b[j] = (multiplier * b[i]) - b[j]

            j = j+1
            
            print("Transformed system\n{0}".format(np.c_[A,b]))

    # backward substitution
    k = n-1

    x = np.zeros(n)
    x[k] = b[k] / A[k,k]

    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:], x[k+1:])) / A[k,k]
        k = k-1
    
    print("Answer array 'x'\n{0}".format(x))

A = np.array([[0.004,15.73],[0.4232,-24.72]])
b = np.array([15.77,-20.49])

print(np.c_[A, b])

print("NUMPY SOLUTION")
gaussian_np(A,b)
print("\nMY SOLUTION")
gaussian_partial(A,b)
