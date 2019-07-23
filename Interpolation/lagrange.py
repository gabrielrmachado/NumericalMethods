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

# x_parabola = np.array([0, 20, 0]) # array for x
# y_parabola = np.array([0, 10, 50]) # array for y
# plt.figure()
# u = plt.plot(x_parabola,y_parabola,'ro') # plot the points
# t = np.linspace(0, 1, len(x_parabola)) # parameter t to parametrize x and y
# pxLagrange = lagrange(t, x_parabola) # X(T)
# pyLagrange = lagrange(t, y_parabola) # Y(T)
# n = 100
# ts = np.linspace(t[0],t[-1],n)
# xLagrange = pxLagrange(ts) # lagrange x coordinates
# yLagrange = pyLagrange(ts) # lagrange y coordinates
# plt.plot(xLagrange, yLagrange,'b-',label = "Polynomial")
# plt.show()

# x_parabola = np.array([0, 20, 0]) # array for x
# y_parabola = np.array([0, 10, 50]) # array for y
# plt.figure()
# u = plt.plot(x_parabola,y_parabola,'ro') # plot the points
# t = np.linspace(0, 1, len(x_parabola)) # parameter t to parametrize x and y
# pxLagrange = lagrange(t, x_parabola) # X(T)
# pyLagrange = lagrange(t, y_parabola) # Y(T)
# n = 100
# ts = np.linspace(t[0],t[-1],n)
# xLagrange = pxLagrange(ts) # lagrange x coordinates
# yLagrange = pyLagrange(ts) # lagrange y coordinates
# plt.plot(xLagrange, yLagrange,'b-',label = "Polynomial")
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# x_points = x
# y_points = y(x)
# p = ax.plot(x_points, y_points, 'r')
# ax.set_xlabel('x-points')
# ax.set_ylabel('y-points')
# plt.show()
