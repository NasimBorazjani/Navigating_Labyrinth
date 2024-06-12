
from collections import deque

def restricted_sorting(stacks):
    costs = {0: 4, 1: 4, 2: 7, 3: 7, 4: 5, 5: 6}
    visited = set()
    queue = deque([(stacks, [], 0)])

    while queue:
        state, moves, cost = queue.popleft()
        visited.add(tuple(map(tuple, state)))

        if is_sorted(state):
            return moves

        for i in range(6):
            if not state[i]:
                continue
            for j in range(6):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]) and len(state[j]) < 4:
                    new_state = [list(s) for s in state]
                    new_state[j].append(new_state[i].pop())
                    new_moves = moves + [(i, j)]
                    new_cost = cost + costs[j]
                    if tuple(map(tuple, new_state)) not in visited:
                        queue.append((new_state, new_moves, new_cost))

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [['Blue', 'Yellow', 'Red', 'Yellow'], ['Green', 'Red', 'Green', 'Red'], ['Blue', 'Green', 'Blue', 'Yellow'], [], [], []]
print(restricted_sorting(stacks))
