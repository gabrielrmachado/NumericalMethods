from scipy.interpolate import lagrange
import numpy as np
import math
import matplotlib.pyplot as plt

x = np.array([0, math.pi/4, math.pi/2, math.pi])
y = np.vectorize((lambda a: math.sin(a)))

testPoint = math.pi/3
f = lagrange(x, y(x))
absError = abs(y(testPoint)-f(testPoint))

print("{0}\nP({1}) = {2}\nAbsolute error: {3:.10f}".format(f, testPoint, f(testPoint), absError))

plt.figure("Lagrange")
plt.plot(np.arange(0.0,10,0.1), y(np.arange(0,10,0.1)), label='True function F(x)')
plt.plot(x, f(x), '--k', label='Interpolation polynomial P(x)')
plt.plot(x, y(x), 'ok', label='Given points')
plt.plot(testPoint, f(testPoint), 'or', label='Test point')
plt.legend()
plt.show()