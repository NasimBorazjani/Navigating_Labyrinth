
def restricted_sorting(stacks, costs):
    moves = []
    while True:
        changed = False
        for i in range(len(stacks)):
            if not stacks[i]:
                continue
            block_color = stacks[i][-1]
            best_cost = float('inf')
            best_stack = -1
            for j in range(len(stacks)):
                if j == i or (stacks[j] and stacks[j][-1] != block_color and len(stacks[j]) < 3):
                    continue
                cost = costs[j]
                if cost < best_cost:
                    best_cost = cost
                    best_stack = j
            if best_stack >= 0:
                stacks[best_stack].append(stacks[i].pop())
                moves.append((i, best_stack))
                changed = True
        if not changed:
            break
    return moves

stacks = [[], [], ['Green', 'Blue', 'Green', 'Yellow'], [], ['Red', 'Red', 'Yellow', 'Blue'], ['Green', 'Red', 'Blue', 'Yellow']]
costs = [2, 4, 6, 6, 6, 7]
print(restricted_sorting(stacks, costs))
