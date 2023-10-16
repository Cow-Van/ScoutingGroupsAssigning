import csv
from person import Person

from utils import assign_groups, clean_data


raw_data: list[list[str]] = []

with open("sheet.csv") as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    for row in reader:
        raw_data.append(row)

cleaned_data = clean_data(raw_data)
people: list[Person] = []

for list in cleaned_data:
    people.append(Person(list[0], list[1], list[2]))

groups = assign_groups(people, 12)

group_names = ["A", "B", "C", "D", "E", "F", "G"]
fields = ["Group", "First Name", "Last Name"]
rows = [[group_names[i], person.first_name, person.last_name] for i, group in enumerate(groups) for person in group]

with open("Scouting Groups.csv", "w") as csvfile:
    write = csv.writer(csvfile)
    write.writerow(fields)
    write.writerows(rows)