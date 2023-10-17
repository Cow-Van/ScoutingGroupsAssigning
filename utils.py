from person import Person


FIRST_NAME_FIELD = "First"
LAST_NAME_FIELD = "Last"
PREF_FIELD = "Pref"

# Remove unnecessary columns
def clean_data(data: list[list[str]]) -> list[list[str]]:
    out: list[list[str]] = []

    first_row = data[0]
    other_rows = data[1:]

    first_name_index = first_row.index(FIRST_NAME_FIELD)
    last_name_index = first_row.index(LAST_NAME_FIELD)
    pref_index = first_row.index(PREF_FIELD)

    for row in other_rows:
        new_row = []
        new_row.append(row[first_name_index])
        new_row.append(row[last_name_index])
        new_row.append(row[pref_index])
        out.append(new_row)

    return out

def search_groups(groups: list[list[Person]], first_name: str, last_name: str) -> int:
    for i, group in enumerate(groups):
        for person in group:
            if person.first_name == first_name and person.last_name == last_name:
                return i

    return -1

def get_pref(list: list[Person], first_name: str, last_name: str) -> Person | None:
    for person in list:
        if person.first_name == first_name and person.last_name == last_name:
            return person

    return None

def assign_to_smallest_group(groups: list[list[Person]], person: Person) -> None:
    smallest_group: list[Person] = groups[0]

    for group in groups[1:]:
        if len(group) < len(smallest_group):
            smallest_group = group
    
    smallest_group.append(person)