
from collections import deque

def restricted_sorting(stacks):
    costs = {0: 3, 1: 6, 2: 3, 3: 2, 4: 1, 5: 1}
    initial_state = tuple(tuple(stack) for stack in stacks)
    goal_state = ((), ('Blue', 'Blue', 'Blue'), (), ('Green', 'Green', 'Green'), ('Yellow', 'Yellow', 'Yellow'), ('Red', 'Red', 'Red'))
    queue = deque([(initial_state, [], 0)])
    visited = {initial_state: 0}

    while queue:
        state, path, cost = queue.popleft()
        if state == goal_state:
            return path
        for i in range(6):
            if not state[i]:
                continue
            for j in range(6):
                if i == j or len(state[j]) == 4 or (state[j] and state[j][0] != state[i][0]):
                    continue
                new_state = list(list(stack) for stack in state)
                new_state[j] = [new_state[i].pop(0)] + new_state[j]
                new_state[i] = tuple(new_state[i])
                new_state[j] = tuple(new_state[j])
                new_state = tuple(new_state)
                new_cost = cost + costs[j]
                if new_state not in visited or new_cost < visited[new_state]:
                    visited[new_state] = new_cost
                    queue.append((new_state, path + [(i, j)], new_cost))

print(restricted_sorting([[], ['Blue', 'Red', 'Blue', 'Red'], [], ['Green', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Blue'], []]))
