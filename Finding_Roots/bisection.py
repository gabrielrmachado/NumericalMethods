import math
import numpy as np

def function(x):
    # return math.pow(math.e, -x) * math.cos(x)
    # return ((math.pow(x,3)) - (7*math.pow(x,2)) + (14*x) - 6)
    return ((32 * math.pow(x,6)) - (48 * math.pow(x,4)) + (18 * math.pow(x,2)) - 1)
    # return math.sin(math.cos(math.pow(math.e, x)))

def bisection(a, b, max_iter, TOL, counter):
    if counter < max_iter:
        counter = counter + 1
        ans1 = function(a)
        ans2 = function(b)
        if abs(ans1) <= TOL:
            print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(counter, a, function(a)))
        elif abs(ans2) <= TOL:
                print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(counter, b, function(b)))
        elif ans1*ans2 < 0:
            p = (a+b)/2
            ans = function(p)
            print("Iter. {0}: f({1}) = {2}".format(counter, p, ans))
            
            if np.sign(ans) == np.sign(ans2):
                bisection(a, p, max_iter, TOL, counter)
            else:
                bisection(p, b, max_iter, TOL, counter)
        else: 
            print("F(a) and F(b) must have opposite signs!")
    else:
        print("Number of max iterations reached. No root was found.")
        
bisection(0.8, 1, 150, 0.001, 0)