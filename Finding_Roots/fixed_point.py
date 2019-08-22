import math
import numpy as np

def f(x):
    # x^3 + 4*x^2 - 10
    # return 0.5 * math.pow((10 - math.pow(x, 3)), 0.5)

    return (math.sin(8*x) + 1) / (math.pow(math.e, x))

    # return x - math.cos(x)
    # return math.cos(x)

def fixed_point(p0, max_iter, TOL, i = 0):
    if (i < max_iter):
        p = f(p0)
        if (abs(p - p0) < TOL):
            print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(i+1, p, abs(p - p0)))
        else:
            print("Iter. {0}: f({1}) = {2}".format(i+1, p, abs(p - p0)))
            i = i+1
            fixed_point(p, max_iter, TOL, i)
    else:
        print("Number of max iterations reached. No root was found.")

fixed_point(0.435, 100, 0.00001)    