
from collections import deque
from itertools import product

def restricted_sorting(stacks):
    costs = {tuple(tuple(stack) for stack in stacks): 0}
    moves = {tuple(tuple(stack) for stack in stacks): []}
    queue = deque([tuple(tuple(stack) for stack in stacks)])

    while queue:
        state = queue.popleft()
        for i, j in product(range(8), repeat=2):
            if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]) and len(state[j]) < 5:
                new_state = list(list(stack) for stack in state)
                new_state[j].append(new_state[i].pop())
                new_state = tuple(tuple(stack) for stack in new_state)
                cost = costs[state] + {0: 2, 1: 1, 2: 2, 3: 8, 4: 4, 5: 3, 6: 6, 7: 3}[j]
                if new_state not in costs or cost < costs[new_state]:
                    costs[new_state] = cost
                    moves[new_state] = moves[state] + [(i, j)]
                    queue.append(new_state)

    sorted_state = tuple(tuple(sorted((color for color in stack if color), reverse=True)) for stack in stacks)
    return moves[sorted_state]

stacks = [['Green', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'Green', 'Red', 'Red', 'Black'], [], ['Blue', 'Yellow', 'Red', 'Black', 'Yellow'], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], []]
print(restricted_sorting(stacks))
