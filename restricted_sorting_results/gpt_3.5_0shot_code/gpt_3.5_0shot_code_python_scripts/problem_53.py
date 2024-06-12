
stacks = [[], ['Blue', 'Green', 'Red', 'Yellow', 'Blue'], ['Green', 'Blue', 'Yellow', 'Black', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Black', 'Black'], ['Green', 'Blue', 'Green', 'Black', 'Red'], [], []]
costs = {0: 7, 1: 4, 2: 1, 3: 2, 4: 6, 5: 8, 6: 7, 7: 6}

def calculate_cost(block, dest_stack):
    if not stacks[dest_stack]:
        return 0
    if stacks[dest_stack][-1] == block:
        return 1
    return costs[dest_stack]

transfers = []

for i in range(len(stacks)):
    if stacks[i]:
        block = stacks[i][-1]
        min_cost = float('inf')
        min_dest = None
        for j in range(len(stacks)):
            if i != j and (not stacks[j] or stacks[j][-1] == block):
                cost = calculate_cost(block, j)
                if cost < min_cost:
                    min_cost = cost
                    min_dest = j
        if min_dest is not None:
            transfers.append((i, min_dest))
            stacks[min_dest].append(stacks[i].pop())

print(transfers)
