# Week 02 - Functions, Modules, and Debugging

## 1. Project Overview

This folder records my second week of learning Python for autonomous driving and engineering applications.

The main focus is dictionaries, functions, modules, command-line arguments, exceptions, variable scope, and a small steering-angle analysis.

## 2. Learning Objectives

- Store and update vehicle data in a dictionary.
- Write reusable functions and import a helper module.
- Read command-line arguments and handle invalid input.
- Practice exception handling and variable scope.
- Calculate travel distance from speed and time.
- Compute steering-angle changes and detect events above a threshold.

## 3. Learning Environment

- Operating System: Windows
- Programming Language: Python
- Code Editor: Visual Studio Code
- Version Control: Git
- Repository Hosting: GitHub

No third-party libraries are required for the scripts in this folder.

## 4. Project Structure

```text
week02/
│
├── day11_vehicle_dict.py
├── debug_sensor.py
├── debug_sensor_exception.py
├── debug_sensor_step.py
├── fibo.py
├── main.py
├── scope_test.py
├── sensor_utils.py
├── vehicle_distance.py
└── vehicle_steering_angle_analysis.py
```

Note: `sensor_utils.py` is a helper module imported by `main.py`. Run `main.py` from the `week02` folder so that import can find the module.

`debug_sensor.py` and `debug_sensor_step.py` currently contain the same code.

## 5. How to Run

Run the scripts from the `week02` folder.

```text
py day11_vehicle_dict.py
py debug_sensor.py
py debug_sensor_exception.py
py scope_test.py
py main.py
py vehicle_steering_angle_analysis.py
```

`fibo.py` is a module that can also be run with a command-line argument. It prints the Fibonacci series up to that number:

```text
py fibo.py 100
```

`vehicle_distance.py` expects two command-line arguments, `<speed>` and `<time>`. The script divides the first argument by 3.6, so that value is treated as a speed in km/h. The second argument is a time in seconds. The printed distance is in meters.

```text
py vehicle_distance.py 72 20
```

If the argument count is wrong, the script prints:

```text
Usage: python vehicle_distance.py <speed> <time>
```

If the arguments are not valid numbers, it prints an error message and exits.

## 6. What the Programs Do

- `day11_vehicle_dict.py` creates a vehicle dictionary, updates the speed, adds a temperature value, deletes the gear, and prints the remaining items.
- `debug_sensor.py` and `debug_sensor_step.py` calculate the average confidence of a short list of detections (car, pedestrian, and truck) and print the result.
- `debug_sensor_exception.py` uses the same average-confidence calculation, but wraps the division in `try` / `except ZeroDivisionError`. In this script the detections list is empty, so it prints `No detections available.` and returns `None`.
- `sensor_utils.py` defines `get_all_objects(sensor_data)`, which flattens all object types from a nested sensor dictionary.
- `main.py` builds sample camera, lidar, and radar detections, calls `get_all_objects`, and prints the flattened list of object types.
- `fibo.py` defines `fib(n)`, which prints the Fibonacci series up to `n`, and `fib2(n)`, which returns that series as a list. When the file is run as a script, it calls `fib()` with the first command-line argument.
- `scope_test.py` shows the difference between local, nonlocal, and global assignment.
- `vehicle_distance.py` calculates travel distance from a command-line speed and time, as described above.
- `vehicle_steering_angle_analysis.py` computes successive steering-angle changes, counts changes whose absolute value is greater than a threshold, and stores the results in a report dictionary. It runs twice: once with angles `[0, 2, 5, 13, 15, 4]` and threshold `7`, and once with `[10, 15, 20, 35, 30, 10]` and threshold `10`.

## 7. Units

- In `vehicle_distance.py`, the first command-line argument is treated as km/h (it is divided by 3.6), time is in seconds, and distance is in meters.
- In `day11_vehicle_dict.py`, `speed` is stored as 72 and later 90, which matches the km/h values used in week 1, but the script itself does not label the unit.
- Steering angles and the event threshold in `vehicle_steering_angle_analysis.py` are used as numeric values; the script does not state their unit.

## 8. Learning Progress

### Week 02

- [x] Create, update, and iterate over a dictionary.
- [x] Write a helper module and import it from another script.
- [x] Read command-line arguments and handle invalid input.
- [x] Handle `ZeroDivisionError` when a detection list is empty.
- [x] Practice local, nonlocal, and global variable scope.
- [x] Calculate travel distance from speed and time.
- [x] Compute steering-angle changes and detect events above a threshold.

## 9. Future Direction

Continue developing Python skills for engineering and autonomous driving applications, including more structured programs, input checks, and tests.
