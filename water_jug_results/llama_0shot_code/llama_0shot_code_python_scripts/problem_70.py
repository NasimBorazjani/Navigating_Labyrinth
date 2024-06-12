
def solve_water_jugs(capacities, amounts):
    actions = []
    for i in range(len(capacities)):
        if amounts[i] <= capacities[i]:
            actions.append(('+', capacities[i], i+1))
        else:
            actions.append(('+', capacities[i], i+1))
            amounts[i+1] += (amounts[i] - capacities[i])
            amounts[i] = capacities[i]
    return actions

capacities = [44, 128, 127, 85, 40, 125]
amounts = [283, 295, 428, 428]

print(solve_water_jugs(capacities, amounts))
