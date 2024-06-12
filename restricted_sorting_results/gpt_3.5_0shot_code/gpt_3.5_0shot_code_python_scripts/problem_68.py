
stacks = [['Black', 'Black', 'White', 'Blue', 'Yellow', 'White'],
          ['Black', 'Blue', 'Red', 'Blue', 'Red', 'Green'],
          [],
          ['Black', 'White', 'Red', 'Green', 'White', 'Blue'],
          ['Yellow', 'Blue', 'Red', 'Green', 'Green', 'Yellow'],
          [],
          ['Green', 'Black', 'Red', 'White', 'Yellow', 'Yellow'],
          [],
          [],
          []]

costs = {0: 9, 1: 11, 2: 2, 3: 10, 4: 8, 5: 6, 6: 4, 7: 4, 8: 7, 9: 3}

transfer_pairs = []

for i in range(len(stacks)):
    for j in range(len(stacks[i])):
        min_cost = float('inf')
        min_dest = -1
        for k in range(len(stacks)):
            if i != k and (len(stacks[k]) == 0 or stacks[k][-1] == stacks[i][j]):
                cost = costs[k]
                if cost < min_cost:
                    min_cost = cost
                    min_dest = k
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i][j])
        stacks[i].pop()

print(transfer_pairs)
