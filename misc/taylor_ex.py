#import pyplot as plt
from sympy import Symbol, summation, pprint, factorial, E
from sympy.plotting import plot


# Plot e(x) as a taylor series
x = Symbol('x')
n = Symbol('n')
e_x = summation(x**n / factorial(n), (n, 0, 5))
pprint(e_x)
p1 = plot(e_x, (x, -10, 10), show=False)
p2 = plot(E**x, (x, -10, 10), show=False)
p1.append(p2[0])
p1.show()
