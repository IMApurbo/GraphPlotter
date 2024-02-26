import matplotlib.pyplot as plt

def plot_straight_line(x_values, y_values):
    # Ensure that the line starts from the origin
    x_values = [0] + x_values
    y_values = [0] + y_values
    
    # Plot the straight line passing through the points
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    
    plt.title('Straight Line with Data Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.grid(True)
    plt.show()

# Input values for x and y axes
x_input = input("Enter values for x (separated by comma): ")
y_input = input("Enter values for y (separated by comma): ")

# Convert input strings to lists of floats
x_values = [float(x) for x in x_input.split(',')]
y_values = [float(y) for y in y_input.split(',')]

plot_straight_line(x_values, y_values)
