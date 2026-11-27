
import numpy as np

# 1. Create a NumPy array
speed = np.array([20, 40, 60, 80, 100])

# 2. Print the array
print(speed)

# 3. Print the shape of the array
print(speed.shape)

# 4. Print the number of dimensions
print(speed.ndim)

# 5. Print the data type
print(speed.dtype)

# Exercise 2.1
# 打印第一个速度 / Print the first speed
print(speed[0])

# Exercise 2.2
# 打印最后一个速度 / Print the last speed
print(speed[-1])

# Exercise 2.3
# 打印第二个到第四个速度
# Print the second through fourth speeds
print(speed[1:4])

# Exercise 2.4
# 打印前三个速度 / Print the first three speeds
print(speed[0:3])

# Exercise 2.5
# 打印最后两个速度 / Print the last two speeds
print(speed[-2:])

speed = np.array([10, 20, 30, 40, 50])

# Calculate the sum
total = np.sum(speed)

# Calculate the mean
average = np.mean(speed)

# Calculate the maximum
maximum = np.max(speed)

# Calculate the minimum
minimum = np.min(speed)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
