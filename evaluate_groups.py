from person import Person
from utils import get_pref, search_groups


def evaluate_groups(groups: list[list[Person]], people: list[Person]) -> float:
    total_people_with_pref = 0
    percent_of_pref_fufilled_sum = 0

    for person in people:
        if len(person.prefs) == 0:
            continue
        
        fullfilled_prefs = 0

        for pref in person.prefs:
            pref_person = get_pref(people, pref.split(" ")[0], pref.split(" ")[1])

            # Check that pref exists
            if pref_person == None:
                continue

            if search_groups(groups, person.first_name, person.last_name) != -1 and search_groups(groups, person.first_name, person.last_name) == search_groups(groups, pref_person.first_name, pref_person.last_name):
                fullfilled_prefs += 1
        
        percent_of_pref_fufilled_sum += fullfilled_prefs / len(person.prefs)
        total_people_with_pref += 1

    if total_people_with_pref == 0:
        return 1

    return percent_of_pref_fufilled_sum / total_people_with_pref