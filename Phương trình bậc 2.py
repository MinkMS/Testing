import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2

# Define the derivative of the function (gradient)
def df(x):
    return 2 * x

# Gradient Descent to find the minimum
def gradient_descent(starting_point, learning_rate, n_iterations):
    x = starting_point
    for i in range(n_iterations):
        gradient = df(x)
        x = x - learning_rate * gradient
    return x

# Parameters
starting_point = 10   # Initial guess
learning_rate = 0.1   # Step size
n_iterations = 100    # Number of iterations

# Find the minimum point using gradient descent
min_x = gradient_descent(starting_point, learning_rate, n_iterations)
min_y = f(min_x)

# Generate values for plotting the function
x_values = np.linspace(-10, 10, 400)
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, color = 'red', label='y = x^2')

# Highlight the minimum point
plt.plot(min_x, min_y, 'ro', label=f'Minimum point at x = {min_x:.2f}, y = {min_y:.2f}')

# Draw the x-axis (y = 0) and y-axis (x = 0)
plt.axhline(0, color = 'blue', linewidth = 1)  # x-axis
plt.axvline(0, color = 'blue', linewidth = 1)  # y-axis

# Add labels and legend
plt.xlabel('x')
plt.ylabel('f(x) = x^2')
plt.title('Graph of y = x^2 and its Minimum Point')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Print the minimum point
print(f"The minimum point is at x = {min_x:.2f}, y = {min_y:.2f}")