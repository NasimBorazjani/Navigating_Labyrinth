
from collections import deque
from copy import deepcopy

def solve(stacks):
    costs = {0: 5, 1: 8, 2: 1, 3: 6, 4: 8, 5: 2, 6: 1, 7: 8}
    initial_state = tuple(tuple(stack) for stack in stacks)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        state, moves = queue.popleft()
        if is_sorted(state):
            return moves
        for i in range(8):
            if not state[i]:
                continue
            for j in range(8):
                if i == j or (state[j] and state[j][0] != state[i][0]):
                    continue
                new_state = deepcopy(state)
                new_state[j] = (new_state[i][0],) + new_state[j]
                new_state[i] = new_state[i][1:]
                new_state = tuple(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

def is_sorted(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True
