
from collections import deque
from itertools import combinations

def restricted_sorting(stacks):
    costs = {0: 1, 1: 3, 2: 3, 3: 8, 4: 7, 5: 9, 6: 8, 7: 8}
    initial_state = tuple(tuple(stack) for stack in stacks)
    goal_state = tuple(tuple(sorted((color for stack in initial_state for color in stack if color == shade), reverse=True)) for shade in sorted(set(color for stack in initial_state for color in stack)))
    queue = deque([(initial_state, [], 0)])
    visited = set([initial_state])
    while queue:
        state, moves, cost = queue.popleft()
        if state == goal_state:
            return moves
        for i, j in combinations(range(8), 2):
            if state[i] and (not state[j] or state[i][-1] == state[j][-1]) and len(state[j]) < 5:
                new_state = list(list(stack) for stack in state)
                new_state[j].append(new_state[i].pop())
                new_state = tuple(tuple(stack) for stack in new_state)
                if new_state not in visited:
                    queue.append((new_state, moves + [(i, j)], cost + costs[j]))
                    visited.add(new_state)
    return []

stacks = [[], [], ['Blue', 'Green', 'Black', 'Blue', 'Red'], ['Green', 'Red', 'Blue', 'Black', 'Blue'], [], ['Red', 'Green', 'Yellow', 'Yellow', 'Black'], ['Green', 'Black', 'Red', 'Yellow', 'Yellow'], []]
print(restricted_sorting(stacks))
