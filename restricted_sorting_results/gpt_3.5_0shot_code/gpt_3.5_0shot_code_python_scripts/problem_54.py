
stacks = [[], ['Green', 'Yellow', 'Blue', 'Yellow', 'Green'], ['Black', 'Yellow', 'Blue', 'Green', 'Red'], ['Red', 'Black', 'Blue', 'Red', 'Black'], [], ['Red', 'Green', 'Yellow', 'Black', 'Blue'], [], []]
costs = {0: 8, 1: 8, 2: 2, 3: 7, 4: 9, 5: 5, 6: 2, 7: 7}

transfer_pairs = []

def get_cost(block, dest_stack):
    if not stacks[dest_stack] or stacks[dest_stack][-1] == block:
        return 1
    else:
        return costs[dest_stack]

for i in range(len(stacks)):
    if stacks[i]:
        block = stacks[i][-1]
        min_cost = float('inf')
        min_dest = -1
        for j in range(len(stacks)):
            if i != j:
                cost = get_cost(block, j)
                if cost < min_cost:
                    min_cost = cost
                    min_dest = j
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i].pop())

print(transfer_pairs)
