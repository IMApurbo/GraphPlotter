import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x_values, y_values):
    # Add a constant term to ensure that the curve passes through the origin
    x_values = np.array(x_values)
    y_values = np.array(y_values)
    x_values = np.insert(x_values, 0, 0)
    y_values = np.insert(y_values, 0, 0)
    
    # Fit a polynomial curve to the data points
    z = np.polyfit(x_values, y_values, len(x_values) - 1)
    p = np.poly1d(z)

    # Generate x values for the curve
    x_curve = np.linspace(0, max(x_values), 100)

    # Plot the curve
    plt.plot(x_curve, p(x_curve), label='Curve Line')

    # Plot the data points
    plt.scatter(x_values[1:], y_values[1:], marker='o', color='red', label='Data Points')

    plt.title('Curve Line with Data Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.legend()
    plt.grid(True)
    plt.show()

# Input values for x and y axes
x_input = input("Enter values for x (separated by comma): ")
y_input = input("Enter values for y (separated by comma): ")

# Convert input strings to lists of floats
x_values = [float(x) for x in x_input.split(',')]
y_values = [float(y) for y in y_input.split(',')]

plot_graph(x_values, y_values)
