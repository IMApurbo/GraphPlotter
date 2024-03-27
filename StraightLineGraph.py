import customtkinter as ctk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to plot the straight line
def plot_straight_line(x_values, y_values):
    fig = Figure(figsize=(6, 4))
    plot = fig.add_subplot(111)
    plot.plot([0] + x_values, [0] + y_values, marker='o', linestyle='-')
    plot.set_title('Straight Line with Data Points')
    plot.set_xlabel('X-axis')
    plot.set_ylabel('Y-axis')
    plot.grid(True)
    return fig

# Function to handle the plotting
def on_plot():
    x_input = x_entry.get()
    y_input = y_entry.get()
    x_values = list(map(float, x_input.split(',')))
    y_values = list(map(float, y_input.split(',')))
    global fig
    fig = plot_straight_line(x_values, y_values)
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
app.title("Plot Straight Line GUI")

# Frame for the plot
plot_frame = ctk.CTkFrame(master=app, width=800, height=400)
plot_frame.pack(pady=20)

# Entries for x and y values
x_entry = ctk.CTkEntry(master=app,width=300, placeholder_text="Enter values for x (separated by comma)")
x_entry.pack(pady=10)

y_entry = ctk.CTkEntry(master=app,width=300, placeholder_text="Enter values for y (separated by comma)")
y_entry.pack(pady=10)

# Plot button
plot_button = ctk.CTkButton(master=app, text="Plot", command=on_plot)
plot_button.pack(pady=10)

# Save as PNG button
save_button = ctk.CTkButton(master=app, text="Save as PNG", command=save_plot)
save_button.pack(pady=10)

# Run the main application loop
app.mainloop()
