import numpy as np
from numpy import linalg as LA

def relative_error(x_c, x_p):
    """
    x_c: current 'x' vector (most updated)
    x_p: previous 'x' vector
    """
    x_sub = np.subtract(x_c, x_p)
    return LA.norm(x_sub, np.inf) / LA.norm(x_c,np.inf)

def jacobi(A, b, TOL = 0.001, seidel = True, w = 1.1):
    n = len(A)
    e = 1
    iterations = 0
    x = np.zeros(n)
    
    while e > TOL:
        x_p = np.copy(x)
        
        for i in range(n):
            A_aux = np.delete(A[i,:], i, 0)
            
            if seidel == False:
                # traditional Jacobi's iteration
                x_aux = np.delete(x_p, i, 0)
            
            else:
                x_aux = np.delete(x, i, 0)
            
            x[i] = ((1 - w) * x[i]) + (w / A[i,i]) * (b[i] - (np.dot(A_aux, x_aux)))
        
        e = relative_error(x, x_p)
        iterations = iterations + 1
            
    print("System converged after {0} iterations.\nSolution array 'x': {1}".format(iterations, x))

A = np.array([[10.,-1.,2.,0.],[-1.,11.,-1.,3.],[2.,-1.,10.,-1.],[0.,3.,-1.,8.]])
b = np.array([6.,25.,-11.,15.])

jacobi(A,b) 
