import matplotlib.pyplot as plt


def fx(x):
    return 1 + 1 / x


# Whatever be the initial value, the final values tends to reach phi(magic ratio).
# even if we start with negative number it jumps quickly to phi.
# The value at which it jumps is 12-13...
y_values = []
x = -0.61803

for _ in range(30):
    result = fx(x)
    y_values.append(result)
    x = result

print(y_values)
plt.plot(y_values)
plt.show()
