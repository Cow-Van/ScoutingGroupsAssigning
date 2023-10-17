from math import ceil
from random import randint
from person import Person
from evaluate_groups import evaluate_groups

def random_groups(groups: list[list[Person]], people: list[list[Person]]):
    best_groups: list[list[Person]] = None
    best_eval: float = 0
    RUNS = 1_000_000

    for count in range(RUNS):
        new_groups: list[list[Person]] = [[] for _ in range(ceil(len(people) / 12))]

        for person in people:
            valid_groups: list[int] = []

            for i, group in enumerate(new_groups):
                if len(group) < 12:
                    valid_groups.append(i)
            
            random_group_index = randint(0, len(valid_groups) - 1)
            new_groups[valid_groups[random_group_index]].append(person)

        new_eval = evaluate_groups(new_groups, people)

        if new_eval > best_eval:
            best_groups = new_groups
            best_eval = new_eval

        print(f"Percent Complete: {count / RUNS}        Best Run: {best_eval}", end="\r")

    print()
    print(best_eval)
    print(best_groups)