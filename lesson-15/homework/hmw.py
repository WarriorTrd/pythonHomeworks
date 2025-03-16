import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import*
from mpl_toolkits.mplot3d import Axes3D
#task 1
# def f(x):
#     return x**2 - 4*x + 4


# x = np.linspace(-10, 10, 100)


# y = f(x)


# plt.plot(x, y, label="f(x) = x² - 4x + 4", color="blue")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("Plot of f(x) = x² - 4x + 4")
# plt.grid(True)
# plt.legend()
# plt.show()


#task 2

# num_points = 100
# x_values = [i * (2 * pi / (num_points - 1)) for i in range(num_points)]


# df = pd.DataFrame({"x": x_values})
# df["sin(x)"] = [sin(x) for x in df["x"]]
# df["cos(x)"] = [cos(x) for x in df["x"]]

# df.plot(x="x", y=["sin(x)", "cos(x)"], title="Sine and Cosine Plot")
# plt.show()

#task 3

x_values = [i / 10 for i in range(-50, 51)]
x_positive = [i / 10 for i in range(0, 51)]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x_values, [x**3 for x in x_values], color="blue")
axes[0, 0].set_title("f(x) = x³")

axes[0, 1].plot(x_values, [sin(x) for x in x_values], color="red")
axes[0, 1].set_title("f(x) = sin(x)")

axes[1, 0].plot(x_values, [exp(x) for x in x_values], color="green")
axes[1, 0].set_title("f(x) = e^x")

axes[1, 1].plot(x_positive, [log(x+1) for x in x_positive], color="purple")
axes[1, 1].set_title("f(x) = log(x+1)")

plt.tight_layout()
plt.show()

#task 4
x_rand = [random.uniform(0, 10) for _ in range(100)]
y_rand = [random.uniform(0, 10) for _ in range(100)]

plt.scatter(x_rand, y_rand, c='blue', marker='o')
plt.title("Random Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()

# task 5
data = [random.gauss(0, 1) for _ in range(1000)]
plt.hist(data, bins=30, alpha=0.7, color="blue")
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# task 6. 3D Plotting
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.cos(X**2 + Y**2)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("3D Surface Plot: f(x, y) = cos(x² + y²)")
plt.colorbar(ax.plot_surface(X, Y, Z, cmap="viridis"))
plt.show()

# task 7. Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=['blue', 'red', 'green', 'purple', 'orange'])
plt.title("Sales Data")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# task 8
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.array([[5, 7, 6, 8], [3, 4, 5, 7], [2, 3, 4, 6]])

plt.bar(time_periods, data[0], label='Category A', color='blue')
plt.bar(time_periods, data[1], bottom=data[0], label='Category B', color='red')
plt.bar(time_periods, data[2], bottom=data[0] + data[1], label='Category C', color='green')

plt.title("Stacked Bar Chart")
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.legend()
plt.show()


