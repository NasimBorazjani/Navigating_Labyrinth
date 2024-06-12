
stacks = [['Black', 'Red', 'Black', 'Green', 'Blue', 'Yellow'],
          ['Yellow', 'Yellow', 'Black', 'Blue', 'Red', 'Green'],
          [],
          [],
          [],
          [],
          ['Yellow', 'Black', 'White', 'Yellow', 'Red', 'Black'],
          ['Green', 'Blue', 'Green', 'White', 'Blue', 'Green'],
          ['Red', 'White', 'Blue', 'White', 'White', 'Red'],
          []]

costs = {0: 11, 1: 8, 2: 4, 3: 6, 4: 4, 5: 3, 6: 6, 7: 9, 8: 5, 9: 10}

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
        if min_dest != -1:
            transfer_pairs.append((i, min_dest))
            stacks[min_dest].append(stacks[i].pop())

print(transfer_pairs)
