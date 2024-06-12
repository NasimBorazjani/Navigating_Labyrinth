
from collections import deque

def restricted_sorting(stacks):
    costs = {0: 3, 1: 6, 2: 5, 3: 6, 4: 1, 5: 1}
    initial_state = tuple(map(tuple, stacks))
    goal_state = (tuple(), ('Yellow', 'Yellow', 'Yellow'), ('Blue', 'Blue', 'Blue'), ('Red', 'Red', 'Red'), tuple(), tuple())
    queue = deque([(initial_state, [])])
    visited = {initial_state: 0}

    while queue:
        current_state, transfers = queue.popleft()
        if current_state == goal_state:
            return transfers
        for i, stack in enumerate(current_state):
            if stack:
                block = stack[-1]
                for j, target in enumerate(current_state):
                    if not target or (len(target) < 4 and target[-1] == block):
                        new_state = list(map(list, current_state))
                        new_state[i] = list(stack[:-1])
                        new_state[j] = list(target) + [block]
                        new_state = tuple(map(tuple, new_state))
                        new_cost = visited[current_state] + costs[j]
                        if new_state not in visited or new_cost < visited[new_state]:
                            visited[new_state] = new_cost
                            queue.append((new_state, transfers + [(i, j)]))
    return []

stacks = [[], ['Yellow', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Red', 'Green'], ['Yellow', 'Blue', 'Yellow', 'Blue'], [], []]
print(restricted_sorting(stacks))
