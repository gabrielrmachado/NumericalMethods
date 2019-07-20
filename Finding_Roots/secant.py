import math, numpy as np

def f(x):
    # return math.pow(x, 3) - 20
    # return math.sin(math.cos(math.pow(math.e, x)))
    # return (20*x - math.pow(x,2)) + (20*math.sqrt(x)) - (x*math.sqrt(x)) + (x*math.sqrt(20-x)) + (math.sqrt(x) * math.sqrt(20-x)) - 155.55
    # return math.pow(x, 7) - 1000
    # return math.pow(x, 3) - 2 *  math.pow(x, 2) - 5
    # return math.pow(x, 3) + 3 *  math.pow(x, 2) - 1
    # return math.pow(x, 3) + math.cos(x)
    return 2 * math.pow(x, 3) + math.log(x)

def error(x0, x1):
    return abs(x1-x0)/abs(x1)

def secant(x0, x1, max_iter, TOL, i=0):
    if (i < max_iter):
        y0 = f(x0)
        y1 = f(x1)
        if abs(y0) < TOL:
            print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(i+1, x0, y0))
        elif abs(y1) < TOL:
            print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(i+1, x1, y1))
        else:
            print("Iter. {0}: f({1}) = {2}".format(i+1, x1, y1))
            i = i+1
            x2 = x1 - ((y1 * (x1 - x0) / (y1 - y0)))
            secant(x1, x2, max_iter, TOL, i)
    else:
        print("Number of max iterations reached. No root was found.")

secant(0.5, 1.5, 100, 0.0001, 0)