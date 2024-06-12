
from collections import deque

def restricted_sorting(stacks):
    costs = {0: 5, 1: 1, 2: 6, 3: 7, 4: 7, 5: 7}
    initial_state = tuple(tuple(stack) for stack in stacks)
    goal_state = ((), (), ('Green', 'Green', 'Green'), ('Red', 'Red', 'Red'), ('Blue', 'Blue', 'Blue'), ('Yellow', 'Yellow', 'Yellow'))
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
                if i == j or (state[j] and state[j][0] != state[i][0]) or len(state[j]) == 4:
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

stacks = [[], [], ['Green', 'Yellow', 'Green', 'Red'], ['Green', 'Red', 'Blue', 'Yellow'], [], ['Blue', 'Red', 'Yellow', 'Blue']]
print(restricted_sorting(stacks))
