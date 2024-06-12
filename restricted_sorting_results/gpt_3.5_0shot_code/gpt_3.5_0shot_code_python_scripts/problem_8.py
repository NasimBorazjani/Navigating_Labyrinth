
stacks = [['Blue', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Green', 'Yellow'], [], [], [], ['Red', 'Blue', 'Red', 'Blue']]
costs = {0: 3, 1: 6, 2: 1, 3: 7, 4: 2, 5: 3}

def find_cheapest_move():
    min_cost = float('inf')
    move = None
    for i in range(len(stacks)):
        if stacks[i]:
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]):
                    c = costs[j]
                    if len(stacks[j]) == 3:
                        c += 1
                    if c < min_cost:
                        min_cost = c
                        move = (i, j)
    return move

transfers = []
while any(stacks):
    move = find_cheapest_move()
    transfers.append(move)
    stacks[move[1]].append(stacks[move[0]].pop())

print(transfers)
