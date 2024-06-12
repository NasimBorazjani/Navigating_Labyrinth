
from collections import deque
from copy import deepcopy

def get_moves(state):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == stack[-1]) and len(target) < 5:
                    moves.append((i, j))
    return moves

def apply_move(state, move):
    new_state = deepcopy(state)
    block = new_state[move[0]].pop()
    new_state[move[1]].append(block)
    return tuple(map(tuple, new_state))

def is_sorted(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def restricted_sorting(stacks):
    costs = {tuple(map(tuple, stacks)): 0}
    moves = {tuple(map(tuple, stacks)): []}
    queue = deque([tuple(map(tuple, stacks))])

    while queue:
        state = queue.popleft()
        for move in get_moves(state):
            new_state = apply_move(state, move)
            cost = costs[state] + {0: 8, 1: 2, 2: 7, 3: 6, 4: 7, 5: 1, 6: 5, 7: 3}[move[1]]
            if new_state not in costs or cost < costs[new_state]:
                costs[new_state] = cost
                moves[new_state] = moves[state] + [move]
                queue.append(new_state)

    sorted_states = [state for state in costs if is_sorted(state)]
    sorted_states.sort(key=costs.get)
    return moves[sorted_states[0]]

stacks = [['Red', 'Red', 'Red', 'Green', 'Yellow'], ['Black', 'Red', 'Green', 'Yellow', 'Yellow'], [], [], [], ['Black', 'Blue', 'Black', 'Yellow', 'Green'], [], ['Blue', 'Green', 'Blue', 'Black', 'Blue']]
print(restricted_sorting(stacks))
