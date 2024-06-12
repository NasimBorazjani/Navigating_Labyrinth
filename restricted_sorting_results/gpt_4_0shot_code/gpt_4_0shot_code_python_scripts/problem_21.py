
from collections import deque

def restricted_sorting(stacks, costs):
    # The goal state is a state where all stacks are either empty or contain blocks of a single shade.
    goal = [sorted(stack) for stack in stacks]

    # The BFS algorithm maintains a queue of nodes to visit.
    queue = deque([(stacks, [])])
    visited = {tuple(map(tuple, stacks)): 0}

    while queue:
        current, path = queue.popleft()

        # When the BFS algorithm finds the goal state, it backtracks from the goal state to the initial state to find the sequence of block transfers that led to the goal state.
        if sorted(current) == goal:
            return path

        for i in range(6):
            if not current[i]:
                continue
            for j in range(6):
                if i != j and (not current[j] or current[j][-1] == current[i][-1]) and len(current[j]) < 4:
                    next = [list(stack) for stack in current]
                    next[j].append(next[i].pop())
                    cost = visited[tuple(map(tuple, current))] + costs[j]
                    if tuple(map(tuple, next)) not in visited or visited[tuple(map(tuple, next))] > cost:
                        visited[tuple(map(tuple, next))] = cost
                        queue.append((next, path + [(i, j)]))

    return []

stacks = [['Red', 'Yellow', 'Blue', 'Yellow'], [], [], ['Green', 'Blue', 'Green', 'Red'], [], ['Yellow', 'Red', 'Green', 'Blue']]
costs = {0: 4, 1: 5, 2: 3, 3: 3, 4: 3, 5: 5}
print(restricted_sorting(stacks, costs))
