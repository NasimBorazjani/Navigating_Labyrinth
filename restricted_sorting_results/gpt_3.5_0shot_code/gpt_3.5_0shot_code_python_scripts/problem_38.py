
stacks = [['Blue', 'Black', 'Yellow', 'Black', 'Red'],
          ['Blue', 'Blue', 'Green', 'Black', 'Yellow'],
          [],
          ['Yellow', 'Red', 'Red', 'Green', 'Green'],
          [],
          [],
          ['Red', 'Blue', 'Black', 'Green', 'Yellow'],
          []]

costs = {0: 7, 1: 5, 2: 7, 3: 2, 4: 6, 5: 7, 6: 5, 7: 3}

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
