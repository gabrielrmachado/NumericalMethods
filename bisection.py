import math

def function(x):
    return math.pow(math.e, -x) * math.cos(x)

def bisection(a, b, max_iter, TOL, counter):
    if counter < max_iter:
        counter = counter + 1
        if abs(function(a)) <= TOL:
            print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(counter, a, function(a)))
        elif abs(function(b)) <= TOL:
                print("Root found on iteration {0}.\nf({1}) = {2:.10f}".format(counter, b, function(b)))
        else:
            p = a + (b-a)/2
            ans = function(p)
            print("Iter. {0}: f({1}) = {2}".format(counter, p, ans))
            
            if (ans > 0):
                bisection(a, p, max_iter, TOL, counter)
            else:
                bisection(p, b, max_iter, TOL, counter)
    else:
        print("Number of max iterations reached. No root was found.")
        
bisection(math.pi, 0, 150, 0.0000000001, 0)