
stacks = [['Red', 'Blue', 'Green', 'Yellow'], ['Blue', 'Blue', 'Green', 'Red'], [], [], [], ['Green', 'Red', 'Yellow', 'Yellow']]
costs = {0: 3, 1: 6, 2: 2, 3: 4, 4: 6, 5: 5}

transfer_pairs = []

def get_cost(block, dest_stack):
    if not stacks[dest_stack]:
        return 1
    elif stacks[dest_stack][-1] == block:
        return 1
    else:
        return costs[dest_stack]

while any(stacks):
    min_cost = float('inf')
    min_transfer = None

    for i, stack in enumerate(stacks):
        if stack:
            block = stack[-1]
            for j in range(6):
                if j != i:
                    cost = get_cost(block, j)
                    if cost < min_cost:
                        min_cost = cost
                        min_transfer = (i, j)

    transfer_pairs.append(min_transfer)
    stacks[min_transfer[1]].append(stacks[min_transfer[0]].pop())

print(transfer_pairs)
