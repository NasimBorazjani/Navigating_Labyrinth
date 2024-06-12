
from collections import deque

def restricted_sorting(stacks, costs):
    initial_state = tuple(tuple(stack) for stack in stacks)
    goal_state = tuple(sorted(stack) for stack in initial_state)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        for i in range(6):
            if not current_state[i]:
                continue
            for j in range(6):
                if i != j and (not current_state[j] or current_state[j][-1] == current_state[i][-1]) and len(current_state[j]) < 4:
                    new_state = list(list(stack) for stack in current_state)
                    new_state[j].append(new_state[i].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [(i, j)]))
    return []

stacks = [['Red', 'Blue', 'Green', 'Yellow'], ['Blue', 'Blue', 'Green', 'Red'], [], [], [], ['Green', 'Red', 'Yellow', 'Yellow']]
costs = {0: 3, 1: 6, 2: 2, 3: 4, 4: 6, 5: 5}
print(restricted_sorting(stacks, costs))
