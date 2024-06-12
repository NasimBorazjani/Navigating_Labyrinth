
from collections import deque
from copy import deepcopy

def bfs(stacks, costs):
    queue = deque([(stacks, [], 0)])
    visited = set()
    while queue:
        stacks, moves, cost = queue.popleft()
        state = tuple(tuple(stack) for stack in stacks)
        if state in visited:
            continue
        visited.add(state)
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves
        for i, stack in enumerate(stacks):
            if stack:
                block = stack[-1]
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == block) and len(target) < 4:
                        new_stacks = deepcopy(stacks)
                        new_stacks[i].pop()
                        new_stacks[j].append(block)
                        new_moves = moves + [(i, j)]
                        new_cost = cost + costs[j]
                        queue.append((new_stacks, new_moves, new_cost))
    return []

stacks = [['Red', 'Green', 'Red', 'Blue'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Blue'], [], []]
costs = {0: 5, 1: 3, 2: 3, 3: 1, 4: 3, 5: 2}
print(bfs(stacks, costs))
