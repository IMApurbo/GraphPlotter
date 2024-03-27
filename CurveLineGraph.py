import customtkinter as ctk
from customtkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Function to plot the graph
def plot_graph(x_values, y_values):
    fig = Figure(figsize=(6, 4))
    plot = fig.add_subplot(111)
    
    # Add a constant term to ensure that the curve passes through the origin
    x_values = np.insert(x_values, 0, 0)
    y_values = np.insert(y_values, 0, 0)
    
    # Fit a polynomial curve to the data points
    z = np.polyfit(x_values, y_values, len(x_values) - 1)
    p = np.poly1d(z)

    # Generate x values for the curve
    x_curve = np.linspace(0, max(x_values), 100)

    # Plot the curve
    plot.plot(x_curve, p(x_curve), label='Curve Line')

    # Plot the data points
    plot.scatter(x_values[1:], y_values[1:], marker='o', color='red', label='Data Points')

    plot.set_title('Curve Line with Data Points')
    plot.set_xlabel('X-axis')
    plot.set_ylabel('Y-axis')

    plot.legend()
    plot.grid(True)
    
    return fig

# Function to handle the plotting
def on_plot():
    x_input = x_entry.get()
    y_input = y_entry.get()
    x_values = [float(x) for x in x_input.split(',')]
    y_values = [float(y) for y in y_input.split(',')]
    
    global fig
    fig = plot_graph(np.array(x_values), np.array(y_values))
    
    # Create a canvas and display the plot
    global canvas
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to save the plot as PNG
def save_plot():
    file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        fig.savefig(file_path)

# Main application window
app = ctk.CTk()
app.title("Curve Line Plot GUI")
app.geometry('800x600')


# Frame for the plot
plot_frame = ctk.CTkFrame(master=app, width=800, height=400)
plot_frame.pack(pady=20)

# Entries for x and y values
x_entry = ctk.CTkEntry(master=app, placeholder_text="Enter values for x (separated by comma)", width=400)
x_entry.pack(pady=10)

y_entry = ctk.CTkEntry(master=app, placeholder_text="Enter values for y (separated by comma)", width=400)
y_entry.pack(pady=10)

# Plot button
plot_button = ctk.CTkButton(master=app, text="Plot", command=on_plot)
plot_button.pack(pady=10)

# Save as PNG button
save_button = ctk.CTkButton(master=app, text="Save as PNG", command=save_plot)
save_button.pack(pady=10)

# Run the main application loop
app.mainloop()
