
import numpy as np

speed = np.array([30, 40, 50, 60, 70])

# 1. Calculate the total speed
# 计算速度总和
total = np.sum(speed)

# 2. Calculate the average speed
# 计算平均速度
average = np.mean(speed)

# 3. Find the maximum speed
# 找出最大速度
maximum = np.max(speed)

# 4. Find the minimum speed
# 找出最小速度
minimum = np.min(speed)

# 5. Calculate the standard deviation
# 计算标准差
std = np.std(speed)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Standard deviation:", std)


import numpy as np

speed = np.array([20, 40, 60, 80, 100])

# 1. Increase every speed by 5
# 每个速度增加 5
speed_add = speed + 5

# 2. Decrease every speed by 10
# 每个速度减少 10
speed_subtract = speed - 10

# 3. Multiply every speed by 3.6
# 每个速度乘以 3.6
speed_multiply = speed * 3.6

# 4. Divide every speed by 2
# 每个速度除以 2
speed_divide = speed / 2

print(speed_add)
print(speed_subtract)
print(speed_multiply)
print(speed_divide)

speed = np.array([10, 20, 30, 40, 50])

# Create time array
# 创建时间数组
time = np.array([2, 2, 2, 2, 2])

# Calculate distance
# 计算每个时间间隔的行驶距离
distance = speed * time

# Calculate total distance
# 计算总距离
total_distance = np.sum(distance)

# Calculate average speed
# 计算平均速度
average_speed = np.mean(speed)

print("Time:", time)
print("Distance:", distance)
print("Total distance:", total_distance)
print("Average speed:", average_speed)


speed = np.array([50, 60, 80, 100])

adjustment = np.array([2, -3, 5, -5])

# Calculate actual speed
# 计算实际速度
actual_speed = speed + adjustment

print(actual_speed)