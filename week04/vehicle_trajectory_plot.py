import numpy as np

# Define vehicle positions
x = np.array([0, 10, 20, 30, 40])
y = np.array([0, 2, 5, 9, 14])

# Combine x and y coordinates
trajectory = np.column_stack((x, y))

# Print trajectory data
print("Vehicle trajectory:")
print(trajectory)

print("Shape:", trajectory.shape)
print("Number of points:", len(trajectory))

import matplotlib.pyplot as plt

# Plot vehicle trajectory
plt.plot(x, y, marker="o", label="Vehicle Trajectory")

# Add labels and title
plt.title("Vehicle Trajectory")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

# Mark the start point
plt.scatter(x[0], y[0], color="green", s=100, label="Start")

# Mark the goal point
plt.scatter(x[-1], y[-1], color="red", s=100, label="Goal")

# Keep equal scaling on both axes
plt.axis("equal")

# Add grid and legend
plt.grid(True)
plt.legend()

# Save figure
plt.savefig("vehicle_trajectory.png", dpi=300, bbox_inches="tight")

# Display figure
plt.show()