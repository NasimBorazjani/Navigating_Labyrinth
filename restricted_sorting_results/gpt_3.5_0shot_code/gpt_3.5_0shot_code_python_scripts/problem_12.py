
stacks = [['Green', 'Yellow', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Yellow'], [], [], ['Blue', 'Red', 'Blue', 'Green'], []]
costs = {0: 2, 1: 2, 2: 3, 3: 7, 4: 1, 5: 7}

transfer_pairs = []

def calculate_cost(block, dest_stack):
    if not stacks[dest_stack]:
        return 1
    elif stacks[dest_stack][-1] == block:
        return 1
    else:
        return costs[dest_stack]

for i in range(len(stacks)):
    if stacks[i]:
        block = stacks[i][-1]
        min_cost = float('inf')
        min_dest = None
        for j in range(len(stacks)):
            if i != j:
                cost = calculate_cost(block, j)
                if cost < min_cost:
                    min_cost = cost
                    min_dest = j
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i].pop())

print(transfer_pairs)
