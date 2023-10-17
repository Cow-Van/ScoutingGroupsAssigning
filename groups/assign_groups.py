from math import ceil
from person import Person
from utils import assign_to_smallest_group, get_pref, search_groups

def assign_groups(people: list[Person], perGroup: int) -> list[list[Person]]:
    groups: list[list[Person]] = [[] for i in range(ceil(len(people) / perGroup))]

    # Sort so that people with least pref get priority
    sorted_people = sorted(people, key=lambda person: len(person.prefs))
    people_no_pref: list[Person] = []
    people_with_pref: list[Person] = []

    for i, sorted_person in enumerate(sorted_people):
        if len(sorted_person.prefs) != 0:
            people_with_pref = sorted_people[i:]
            break

        people_no_pref.append(sorted_people[i])

    next_groups_index = 0
    unassigned_people_with_pref: list[Person] = []

    for person_with_pref in people_with_pref:
        if search_groups(groups, person_with_pref.first_name, person_with_pref.last_name) != -1:
            continue

        assigned = False

        for pref in person_with_pref.prefs:
            pref_person = get_pref(people, pref.split(" ")[0], pref.split(" ")[1])

            # Checks if pref is people list
            if pref_person == None:
                continue

            pref_groups_index = search_groups(groups, pref_person.first_name, pref_person.last_name)

            # Check if pref is already in a group. if yes: try to add to group; if no: add them together to next group
            if pref_groups_index != -1:
                # Check if group has space. if yes: add to space & exit loop; if no: move on to next pref
                if len(groups[pref_groups_index]) < perGroup:
                    groups[pref_groups_index].append(person_with_pref)
                    assigned = True
                    break
            else:
                # Add both to new group
                (groups[next_groups_index]).append(person_with_pref)
                groups[next_groups_index].append(pref_person)
                assigned = True
                break
        
        # Check if person_with_pref was assigned to a group. if yes: update next_groups_index to next index; if no: add person_with_pref to person_with_pref
        if assigned:
            next_groups_index += 1

            if next_groups_index >= len(groups):
                next_groups_index = 0

            while len(groups[next_groups_index]) >= perGroup:
                next_groups_index += 1

                if next_groups_index >= len(groups):
                    next_groups_index = 0
        else:
            unassigned_people_with_pref.append(person_with_pref)

    # Assign unassigned_people_with_pref to groups
    for unassigned_person_with_pref in unassigned_people_with_pref:
        if search_groups(groups, unassigned_person_with_pref.first_name, unassigned_person_with_pref.last_name) == -1:
            assign_to_smallest_group(groups, unassigned_person_with_pref)

    # Assign people_no_pref to groups
    for person_no_pref in people_no_pref:
        if search_groups(groups, person_no_pref.first_name, person_no_pref.last_name) == -1:
            assign_to_smallest_group(groups, person_no_pref)

    return groups
