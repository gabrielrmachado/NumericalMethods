import math

def function(x):
    # return math.pow(math.e, -x) * math.cos(x)
    return math.pow(math.e, x)
    # return 4 * math.pow(x, 3) + 3 *  math.pow(x, 2) - 7*x

def ddx_function(x):
    # return (- math.pow(math.e, -x) * (math.sin(x) + math.cos(x)))
    return (math.pow(math.e, x))
    # return 12 * math.pow(x, 2) + 6*x - 7
    
def newton_raphson(x, i=0, max_iter = 50, TOL = 0.000000001):
    ans = function(x)
    if (i < max_iter):
        if (abs(ans) <= TOL):
             print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(i+1, x, ans))    
        else:
            x1 = x - (ans/ddx_function(x))    
            i = i + 1
            newton_raphson(x1, i)
    else:
        print("Number of max iterations reached. No root was found.")

newton_raphson(-10)
