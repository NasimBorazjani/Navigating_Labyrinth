
from collections import deque

def bfs(stacks, costs):
    queue = deque([(stacks, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        # Check if the current state is the goal state
        if all(len(set(stack)) <= 1 for stack in state):
            return path

        # Generate all possible next states
        for i, stack in enumerate(state):
            if stack:
                for j, cost in costs.items():
                    if i != j and (not state[j] or state[j][-1] == stack[-1]):
                        next_state = state[:]
                        next_state[i] = stack[:-1]
                        next_state[j] = state[j] + [stack[-1]]
                        next_path = path + [(i, j)]
                        queue.append((next_state, next_path))

    return []

stacks = [[], [], ['Green', 'Red', 'Black', 'Blue', 'Blue'], ['Yellow', 'Blue', 'Blue', 'Green', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Red', 'Black'], [], [], ['Red', 'Green', 'Green', 'Red', 'Black']]
costs = {0: 2, 1: 3, 2: 9, 3: 8, 4: 3, 5: 7, 6: 9, 7: 5}
print(bfs(stacks, costs))
