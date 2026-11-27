import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)

# Find the first derivative
dy = np.cos(x)

# Find the second derivative
d2y = -np.sin(x)

# Calculate curvature
k = np.abs(d2y) / (1 + dy**2)**(3 / 2)

# Find the point closest to x = pi/2
diff_pi_2 = np.abs(x - np.pi / 2)
index_closest = np.argmin(diff_pi_2)

x_point = x[index_closest]
y_point = y[index_closest]
k_point = k[index_closest]

print(
    f"Closest point: x={x_point:.4f}, "
    f"y={y_point:.4f}, curvature={k_point:.4f}"
)

# Create two subplots
fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(9, 6),
    sharex=True
)

# Plot sine function
ax1.plot(x, y, label="Sine Function")

# Mark the selected point on the sine curve
ax1.scatter(x_point, y_point, color="red", zorder=3)

ax1.annotate(
    f"({x_point:.2f}, {y_point:.2f})",
    xy=(x_point, y_point),
    xytext=(10, -25),
    textcoords="offset points",
    color="red",
    arrowprops=dict(arrowstyle="->", color="red")
)

ax1.set_title("Sine Function")
ax1.set_ylabel("y")
ax1.grid(True)
ax1.legend()

# Plot curvature
ax2.plot(x, k, color="red", label="Curvature")

# Mark the selected point on the curvature curve
ax2.scatter(x_point, k_point, color="blue", zorder=3)

ax2.annotate(
    f"({x_point:.2f}, {k_point:.2f})",
    xy=(x_point, k_point),
    xytext=(-30, -30),
    textcoords="offset points",
    color="blue",
    arrowprops=dict(arrowstyle="->", color="blue")
)

ax2.set_title("Curvature of Sine Function")
ax2.set_xlabel("x")
ax2.set_ylabel(r"Curvature $\kappa$ (1/length)")
ax2.grid(True)
ax2.legend()

# Set X-axis ticks
ticks = [
    0,
    np.pi / 2,
    np.pi,
    3 * np.pi / 2,
    2 * np.pi
]

tick_labels = [
    "0",
    r"$\pi/2$",
    r"$\pi$",
    r"$3\pi/2$",
    r"$2\pi$"
]

ax1.set_xticks(ticks)
ax1.set_xticklabels(tick_labels)

ax2.set_xticks(ticks)
ax2.set_xticklabels(tick_labels)

# Adjust layout and save figure
plt.tight_layout()

fig.savefig(
    "sine_curvature.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()