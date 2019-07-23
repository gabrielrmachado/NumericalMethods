from scipy.interpolate import lagrange
import numpy as np
import math
import matplotlib.pyplot as plt

x = np.array([1.0, 5.7, 15])
y = np.vectorize((lambda a: a * math.log(a)))

testPoint = 10
f = lagrange(x, y(x))
absError = abs(y(testPoint)-f(testPoint))

print("{0}\nP({1}) = {2}\nAbsolute error: {3:.10f}".format(f, testPoint, f(testPoint), absError))

plt.figure()
plt.plot([1,3,6,9,12,18], y([1,3,6,9,12,18]), label='True function F(x)')
plt.plot(x, f(x), '--k', label='Interpolation polynomial P(x)')
plt.plot(x, y(x), 'ok', label='Given points')
plt.legend()
plt.show()