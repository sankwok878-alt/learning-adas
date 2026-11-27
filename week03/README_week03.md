# Week 03 - Data Structures, Beam Deflection, and Tests

## 1. Project Overview

This folder records my third week of learning Python for autonomous driving and engineering applications.

The main focus is lists, tuples, sets, dictionaries, and list comprehensions, together with a structured beam-deflection program that validates inputs, writes results to a CSV file, and is checked with pytest.

## 2. Learning Objectives

- Practice lists, tuples, sets, nested dictionaries, and list comprehensions.
- Work with example sensor detection data.
- Split a beam-deflection calculation into a module, a main program, and tests.
- Validate function inputs and raise ValueError.
- Save calculation results to a CSV file and read them back.
- Run unit tests with pytest.

## 3. Learning Environment

- Operating System: Windows
- Programming Language: Python
- Libraries: pytest (for the beam tests)
- Code Editor: Visual Studio Code
- Version Control: Git
- Repository Hosting: GitHub

The other scripts in this folder use only the Python standard library (`csv` and `pathlib` in `beam_main.py`).

## 4. Project Structure

```text
week03/
│
├── beam.py
├── beam_main.py
├── beam_results.csv
├── flatten.py
├── matrix_transpose.py
├── sensor_dict.py
├── sensor_processing.py
├── speed_analysis.py
├── test_beam.py
└── tuples_sets.py
```

Note: `beam_main.py` writes to and reads `beam_results.csv` in the current working directory, so run that program from the `week03` folder. `test_beam.py` imports `calculate_deflection` from `beam.py`, so run pytest from this folder as well.

## 5. How to Run

Install pytest if needed, then run the programs from the `week03` folder.

```text
py -m pip install pytest
py beam_main.py
py -m pytest test_beam.py
```

`beam_main.py` asks for `q`, `L`, `E`, and `I`, prints the deflection, appends one row to `beam_results.csv`, and then prints all saved records. Running it again will add another row to the CSV.

The data-structure exercises can be run with:

```text
py tuples_sets.py
py sensor_dict.py
py sensor_processing.py
py matrix_transpose.py
py flatten.py
py speed_analysis.py
```

`tuples_sets.py`, `sensor_dict.py`, `sensor_processing.py`, and `matrix_transpose.py` print results. `flatten.py` and `speed_analysis.py` compute values but do not print them.

## 6. What the Programs Do

### Beam deflection

`beam.py` defines `calculate_deflection(q, L, E, I)` for the maximum deflection of a simply supported beam under a uniform load:

δ = 5qL^4 / 384EI

The function checks the inputs before calculating:

- `q` may be zero, but must not be negative.
- `L`, `E`, and `I` must be greater than 0.

Invalid values raise `ValueError`.

`beam_main.py` asks for the four inputs, calls `calculate_deflection`, prints the deflection in meters and millimeters, and appends a row to `beam_results.csv`. The CSV columns are:

`q_N_per_m`, `L_m`, `E_Pa`, `I_m4`, `deflection_m`, `deflection_mm`

The file currently has two data rows:

- q = 1000 N/m, L = 4 m, E = 2.1e11 Pa, I = 8e-6 m^4, deflection = 0.001984 m (1.984127 mm)
- q = 2000 N/m, L = 5 m, E = 2.1e11 Pa, I = 8e-6 m^4, deflection = 0.009688 m (9.688120 mm)

`test_beam.py` contains six tests. All six passed when run with `pytest`:

- `test_example_values`: for q = 1000 N/m, L = 4 m, E = 2.1e11 Pa, and I = 8e-6 m^4, the deflection is approximately 0.001984127 m.
- `test_zero_load`: a zero uniform load produces zero deflection.
- `test_double_load_doubles_deflection`: doubling q doubles the deflection.
- `test_negative_load_raises`: a negative q raises `ValueError`.
- `test_zero_length_raises`: L = 0 raises `ValueError`.
- `test_zero_modulus_raises`: E = 0 raises `ValueError`.

### Data-structure exercises

- `tuples_sets.py` unpacks `(label, confidence)` detections, builds a set of unique labels, and uses set operations on camera and lidar object sets (intersection, union, and camera-only difference).
- `sensor_dict.py` stores camera, lidar, and radar data in a nested dictionary, updates some values, adds a GPS entry, and prints all keys and values.
- `sensor_processing.py` prints each detection from camera, lidar, and radar, then builds unique object types, high-confidence detections (confidence >= 0.9), per-sensor counts, and set comparisons between camera and lidar. Those later collections are computed but not printed.
- `flatten.py` flattens a nested list of objects with a nested loop and with a list comprehension, then builds a set of unique objects. It does not print the results.
- `matrix_transpose.py` transposes a 3x3 list of lists with `zip(*vehicle_data)` and prints the result.
- `speed_analysis.py` starts from a list of speeds in km/h, builds a list of speeds of at least 80 km/h, and converts speeds to m/s with list comprehensions. It does not print the results.

## 7. Units

- Uniform load `q` is in N/m.
- Beam length `L` is in m.
- Modulus of elasticity `E` is in Pa.
- Moment of inertia `I` is in m^4.
- Deflection is stored and printed in meters (`deflection_m`) and millimeters (`deflection_mm`).
- In `speed_analysis.py`, speeds start in km/h and are converted to m/s by dividing by 3.6.

## 8. Learning Progress

### Week 03

- [x] Practice tuples, sets, nested dictionaries, and list comprehensions.
- [x] Work with example camera, lidar, and radar detection data.
- [x] Implement `calculate_deflection` with input checks and `ValueError`.
- [x] Run a main program that prints deflection in m and mm and appends results to a CSV file.
- [x] Write six pytest tests for the beam calculation.
- [x] Save two beam-deflection records in `beam_results.csv`.

## 9. Future Direction

Continue developing Python skills for engineering and autonomous driving applications, including numerical computing and data analysis with the libraries used in later weeks.
