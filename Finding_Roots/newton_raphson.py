import math

def function(x):
        # return math.pow(math.e, -x) * math.cos(x)
        # return math.pow(math.e, x)
        # return 4 * math.pow(x, 3) + 3 *  math.pow(x, 2) - 7*x
        # return ((math.pow(x,3)) - (7*math.pow(x,2)) + (14*x) - 6)
        # return (x * math.pow(math.e, x) - math.sin(8*x) - 1)
        # return math.cos(x) - x
        # return math.pow(x, 3) - 2 *  math.pow(x, 2) - 5
        # return math.pow(x, 3) + 3 *  math.pow(x, 2) - 1
        # return math.pow(x, 3) + math.cos(x)
        # return 2 * math.pow(x, 3) + math.log(x)
        return math.pow(x, 2) - 2

def ddx_function(x):
        # return (- math.pow(math.e, -x) * (math.sin(x) + math.cos(x)))
        # return (math.pow(math.e, x))
        # return 3 * math.pow(x, 2) - 14*x + 14
        # return ((math.pow(math.e, x) * (x+1)) - 8*math.cos(8*x))
        # return - math.sin(x) - 1
        # return 3 * math.pow(x, 2) - 4*x
        # return 3 * math.pow(x, 2) + 6*x
        # return 3 * math.pow(x, 2) - math.sin(x)
        # return (6 * math.pow(x, 2)) + (1/x)
        return 2*x
    
def newton_raphson(x, i=0, max_iter = 50, TOL = 0.0001):
    ans = function(x)
    if (i < max_iter):
        if (abs(ans) <= TOL):
             print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(i+1, x, ans))    
        else:
            print("Iter. {0}: f({1}) = {2}".format(i+1, x, ans))
            x1 = x - (ans/ddx_function(x))    
            i = i + 1
            newton_raphson(x1, i)
    else:
        print("Number of max iterations reached. No root was found.")

def error(x0, x1):
    return abs(x1-x0)/abs(x1)

def newton_sqrt(x, TOL = 0.00000001):
        a = x
        found = False
        for i in range(100):
                xn = 0.5 * (x + (a/x))
                print("Iter. {0}: sqrt({1}) = {2}".format(i, a, x))
                if error(xn, x) <= TOL:
                        found = True   
                        print("SQRT({0}) found on iteration {1} = {2}".format(a, i, xn))
                        break                      
                x = xn
        if not found:
               print("Number of max iterations reached. No SQRT was found.") 

# newton_raphson(2)
newton_sqrt(2)