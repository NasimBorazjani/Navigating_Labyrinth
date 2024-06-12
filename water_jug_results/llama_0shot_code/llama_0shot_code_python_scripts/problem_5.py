
def solve_water_jug_problem():
    jugs = [(145, 'A'), (101, 'B'), (17, 'C'), (75, 'D'), (102, 'E'), (129, 'F')]  # capacities and labels
    buckets = [260, 287, 413]  # target volumes
    actions = []  # list to store the actions
    jug_dict = {jug[1]: jug[0] for jug in jugs}  # dictionary to access jug capacities by their labels

    for i, bucket in enumerate(buckets):
        current_jug = None
        while bucket > 0:
            if current_jug is None or jug_dict[current_jug] <= bucket:
                current_jug = max(jug_dict, key=lambda k: jug_dict[k] if jug_dict[k] <= bucket else 0)
            if jug_dict[current_jug] <= bucket:
                actions.append(('+', current_jug, i+1))
                bucket -= jug_dict[current_jug]
            else:
                actions.append(('+', current_jug, i+1))
                jug_dict[current_jug] = 0
        jug_dict[current_jug] = 0

    return actions

print(solve_water_jug_problem())
