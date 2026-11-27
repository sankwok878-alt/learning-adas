# Week 04 - NumPy, Matplotlib and Pandas

## 1. Project Overview

This folder records my fourth week of learning Python for autonomous driving and engineering applications.

The main focus is using NumPy for numerical computing, Matplotlib for data visualization, and Pandas for basic data analysis.

## 2. Learning Objectives

- Learn how to create and manipulate NumPy arrays.
- Perform numerical calculations with NumPy.
- Use Matplotlib to plot mathematical functions and vehicle trajectories.
- Calculate and visualize the curvature of a sine curve.
- Use Pandas to read a CSV file and calculate basic statistics.

## 3. Learning Environment

- Operating System: Windows
- Programming Language: Python
- Libraries: NumPy, Matplotlib, Pandas
- Code Editor: Visual Studio Code
- Version Control: Git
- Repository Hosting: GitHub

## 4. Project Structure

```text
week04/
│
├── beam_stats.py
├── numpy_basics.py
├── numpy_operations.py
├── numpy_vehicle_analysis.py
├── sine_curvature.py
├── sine_curvature.png
├── sine_trajectory.py
└── vehicle_trajectory_plot.py
```

Note: `beam_stats.py` reads `../week03/beam_results.csv`. The CSV file is stored in the `week03` folder.

## 5. How to Run

Install the libraries, then run the scripts from the `week04` folder. Running them here matters, because `beam_stats.py` uses the relative path `../week03/beam_results.csv` to find the CSV.

```text
py -m pip install numpy matplotlib pandas
py sine_curvature.py
py beam_stats.py
```

## 6. What the Plots Show

`sine_curvature.png` has two subplots in one figure:

- The sine trajectory y = sin(x)
- The curvature κ of that curve

Check point: at the sample closest to x = π/2, κ ≈ 1.

## 7. Units

- x is in radians.
- Curvature κ is in 1/length.
- Deflection is in meters (`deflection_m`) and millimeters (`deflection_mm`).

## 8. Learning Progress

### Week 04

- [x] Create NumPy arrays and inspect array properties.
- [x] Perform numerical calculations with NumPy.
- [x] Generate two-dimensional vehicle trajectory data.
- [x] Plot sine curves and vehicle trajectories with Matplotlib.
- [x] Use labels, legends, grids, and equal axis scaling.
- [x] Calculate the curvature of a sine curve using its first and second derivatives.
- [x] Visualize the sine curve and its curvature in separate subplots.
- [x] Read CSV files with Pandas and calculate mean, minimum, maximum, and non-null count.

## 9. Future Direction

Continue developing Python skills for engineering and autonomous driving applications. Build on the current NumPy, Matplotlib, and Pandas foundations through further numerical analysis, data processing, and practical vehicle-related exercises.
