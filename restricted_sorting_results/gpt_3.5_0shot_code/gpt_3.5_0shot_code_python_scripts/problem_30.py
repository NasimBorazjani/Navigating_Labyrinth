
stacks = [[], ['Blue', 'Red', 'Blue', 'Red'], [], ['Green', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Blue'], []]
costs = {0: 3, 1: 6, 2: 3, 3: 2, 4: 1, 5: 1}
transfer_pairs = []

def get_cost(block, dest_stack):
    if not stacks[dest_stack] or stacks[dest_stack][-1] == block:
        return 1
    else:
        return costs[dest_stack]

for i, stack in enumerate(stacks):
    if stack:
        block = stack[-1]
        min_cost = float('inf')
        min_dest = None
        for dest_stack in range(len(stacks)):
            if dest_stack != i:
                cost = get_cost(block, dest_stack)
                if cost < min_cost:
                    min_cost = cost
                    min_dest = dest_stack
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i].pop())

print(transfer_pairs)
