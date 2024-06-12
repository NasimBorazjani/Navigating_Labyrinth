
stacks = [['Green', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'Green', 'Red', 'Red', 'Black'], [], ['Blue', 'Yellow', 'Red', 'Black', 'Yellow'], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], []]
costs = {0: 2, 1: 1, 2: 2, 3: 8, 4: 4, 5: 3, 6: 6, 7: 3}

transfer_pairs = []

def find_cheapest_move():
    min_cost = float('inf')
    from_stack = -1
    to_stack = -1

    for i in range(len(stacks)):
        if stacks[i]:
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]):
                    cost = costs[i]
                    if i != j:
                        cost += 1
                    if cost < min_cost:
                        min_cost = cost
                        from_stack = i
                        to_stack = j

    return from_stack, to_stack

while any(stacks):
    from_stack, to_stack = find_cheapest_move()
    transfer_pairs.append((from_stack, to_stack))
    stacks[to_stack].append(stacks[from_stack].pop())

print(transfer_pairs)
