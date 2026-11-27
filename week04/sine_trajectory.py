import numpy as np

# Generate x values
x = np.linspace(0, 2 * np.pi, 100)

# Generate y values (sine of x)
y = np.sin(x)


import matplotlib.pyplot as plt
# Plot sine wave
plt.plot(
    x,
    y,
    label="sin(x)",
    color="blue",
    linewidth=2,
    marker="o",
    markersize=3
)

# Add title and axis labels
plt.title("Sine Wave")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")

plt.legend()
# Add grid
plt.grid(True)

# Display the plot
plt.show()