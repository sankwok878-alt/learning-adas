import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    if file.tell() == 0:
        writer.writeheader()
    writer.writerow({"name": name, "home": home})