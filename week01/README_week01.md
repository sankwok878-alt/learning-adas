# Week 01 - Python Basics and First Engineering Exercises

## 1. Project Overview

This folder records my first week of learning Python for autonomous driving and engineering applications.

The main focus is Python syntax, functions, user input, and two simple calculations: vehicle speed and distance, and simply supported beam deflection.

## 2. Learning Objectives

- Practice Python syntax, functions, and return values.
- Use conditional statements, loops, lists, and dictionaries.
- Convert vehicle speed from km/h to m/s and calculate travel distance.
- Read user input and print results with units.
- Calculate the maximum deflection of a simply supported beam from uniform load, length, modulus of elasticity, and moment of inertia.

## 3. Learning Environment

- Operating System: Windows
- Programming Language: Python
- Code Editor: Visual Studio Code
- Version Control: Git
- Repository Hosting: GitHub

No third-party libraries are required for the scripts in this folder.

## 4. Project Structure

```text
week01/
│
├── beam_deflection.py
├── day01_functions.py
├── day01_vehicle.py
├── grade.py
├── number.py
├── python_review.py
├── speed_error.py
├── steel_sections.py
├── test_vehicle.py
├── vehicle_input.py
├── vehicle_kinematics.py
└── vehicle_speed_check.py
```

Note: `test_vehicle.py` is present in the folder, but it is currently an empty file.

## 5. How to Run

Run the scripts from the `week01` folder. These programs use only the Python standard library.

Scripts that use fixed data can be run directly:

```text
py day01_vehicle.py
py python_review.py
py steel_sections.py
py vehicle_kinematics.py
py number.py
```

These scripts ask for keyboard input: `day01_functions.py`, `vehicle_input.py`, `vehicle_speed_check.py`, `speed_error.py`, `grade.py`, and `beam_deflection.py`. For example:

```text
py beam_deflection.py
```

## 6. What the Programs Do

- `day01_vehicle.py` uses a speed of 72 km/h and a time of 20 s, converts the speed to m/s, and prints the travel distance.
- `vehicle_input.py` and `day01_functions.py` do the same speed and distance calculation from user input. `day01_functions.py` puts the conversion and the distance calculation into functions.
- `vehicle_kinematics.py` repeats the calculation for three vehicles, using lists, a list comprehension, and `zip`.
- `python_review.py` starts from a list of speeds in km/h, drops zeros, converts the remaining values to m/s, sorts them in descending order, prints a ranking with `enumerate()`, and prints the average speed.
- `vehicle_speed_check.py` classifies a speed as Fast (above 100 km/h), Cruising (60 km/h or above), or Slow.
- `speed_error.py` calculates the difference between a target speed and an actual speed, and also prints the absolute error, both in km/h.
- `grade.py` converts a numeric score to a letter grade and rejects scores outside 0 to 100.
- `steel_sections.py` stores steel section data in a list of dictionaries, sorts the sections by area in descending order, and prints the sections whose `Ix` is greater than 4000.
- `beam_deflection.py` calculates the maximum deflection of a simply supported beam under a uniform load, using δ = 5qL^4 / 384EI. It prints the result in meters and millimeters. This version only performs the calculation; it does not validate the inputs or save a CSV file.
- `number.py` is a short function-argument example that prints a fixed message.

## 7. Units

- Vehicle speed is entered or stored in km/h and converted to m/s by dividing by 3.6.
- Travel time is in seconds.
- Travel distance is in meters.
- Speed error is in km/h.
- For the beam calculation: uniform load `q` is in N/m, length `L` is in m, modulus of elasticity `E` is in Pa, and moment of inertia `I` is in m^4. Deflection is printed in meters and millimeters.

The `area` and `Ix` values in `steel_sections.py` are used as stored numbers; the script does not state their units.

## 8. Learning Progress

### Week 01

- [x] Practice Python basic syntax, functions, and return values.
- [x] Use conditional statements, including input checks in `grade.py`.
- [x] Use loops, lists, dictionaries, and sorting.
- [x] Convert vehicle speed from km/h to m/s and calculate travel distance.
- [x] Calculate simply supported beam deflection from user input.

## 9. Future Direction

Continue developing Python skills for engineering and autonomous driving applications, including more structured functions, data handling, and checks on calculation inputs.
