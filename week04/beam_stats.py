import pandas as pd
df = pd.read_csv(r"D:\projects\learning-adas\week03\beam_results.csv")
print(df)

#calculate the mean of deflection_m
deflection_mean = df["deflection_m"].mean()

#calculate the min of deflection_m
deflection_min = df["deflection_m"].min()

#calculate the max of deflection_m
deflection_max = df["deflection_m"].max()

#calculate the number of deflection_m
deflection_count = df["deflection_m"].count()

print("Mean deflection:", deflection_mean, "m")
print("Minimum deflection:", deflection_min, "m")
print("Maximum deflection:", deflection_max, "m")
print("Valid data count:", deflection_count, "m")