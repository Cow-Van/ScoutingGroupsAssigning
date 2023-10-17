import csv
from math import ceil
from random import randint
from assign_groups import assign_groups
from evaluate_groups import evaluate_groups
from person import Person
from utils import clean_data


raw_data: list[list[str]] = []

with open("sheet.csv") as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    for row in reader:
        raw_data.append(row)

cleaned_data = clean_data(raw_data)
people: list[Person] = []

for person_data in cleaned_data:
    people.append(Person(person_data[0], person_data[1], person_data[2]))

groups = assign_groups(people, 12)

group_names = ["A", "B", "C", "D", "E", "F", "G"]
fields = ["Group", "First Name", "Last Name"]
rows = [[group_names[i], person.first_name, person.last_name] for i, group in enumerate(groups) for person in group]

# Eval
print(evaluate_groups(groups, people))

with open("Scouting Groups.csv", "w") as csvfile:
    write = csv.writer(csvfile)
    write.writerow(fields)
    write.writerows(rows)