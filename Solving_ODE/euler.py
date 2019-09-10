import numpy as np
import math

def Y_derivative(ti,yi):
    return yi - math.pow(ti,2) + 1
    # return ti * math.pow(math.e,3*ti) - (2*yi)
    # return 1 + (ti-yi)**2
    # return 1 + (yi/ti)
    # return math.e**(ti-yi)

def euler_method(a, b, h, y_0):
    """
    a: lower number in interval
    b: higher number in interval
    h: step size
    F_d: y' (given derivative)
    y_0: point 'y' from initial condition 
    """
    ti = a
    yi = y_0
    i = 0.0
    
    print("APROXIMATED POINTS (ti, yi)\n")
    while ti <= b:
        print("({0:.2f}, {1:.7f})".format(ti,yi))
        yi = yi + Y_derivative(ti,yi) * h # euler's method
        i = i + 1.0
        ti = a + i*h
        
euler_method(0., 2., 0.2, 0.5)