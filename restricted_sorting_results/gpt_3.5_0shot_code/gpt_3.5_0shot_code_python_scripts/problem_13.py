
stacks = [['Green', 'Red', 'Blue', 'Blue'], [], ['Yellow', 'Red', 'Green', 'Green'], [], [], ['Red', 'Yellow', 'Blue', 'Yellow']]
costs = {0: 4, 1: 2, 2: 2, 3: 7, 4: 4, 5: 5}

def find_cheapest_move():
    min_cost = float('inf')
    move = None
    for i in range(len(stacks)):
        if stacks[i]:
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]):
                    if len(stacks[j]) < 4 or stacks[j][-1] == stacks[i][-1]:
                        if costs[j] < min_cost:
                            min_cost = costs[j]
                            move = (i, j)
    return move

moves = []
while any(stacks):
    move = find_cheapest_move()
    if move:
        blocks = stacks[move[0]].pop()
        stacks[move[1]].append(blocks)
        moves.append(move)

print(moves)
