
from collections import deque
from copy import deepcopy

def bfs(stacks, costs):
    queue = deque([(stacks, [], 0)])
    visited = set([tuple(map(tuple, stacks))])
    while queue:
        stacks, moves, cost = queue.popleft()
        if is_goal(stacks):
            return moves
        for i in range(6):
            if not stacks[i]:
                continue
            for j in range(6):
                if i == j or len(stacks[j]) == 4 or (stacks[j] and stacks[j][-1] != stacks[i][-1]):
                    continue
                new_stacks = deepcopy(stacks)
                block = new_stacks[i].pop()
                new_stacks[j].append(block)
                new_moves = moves + [(i, j)]
                new_cost = cost + costs[j]
                if tuple(map(tuple, new_stacks)) not in visited:
                    visited.add(tuple(map(tuple, new_stacks)))
                    queue.append((new_stacks, new_moves, new_cost))
    return []

def is_goal(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [[], ['Green', 'Blue', 'Yellow', 'Green'], ['Yellow', 'Red', 'Red', 'Blue'], [], ['Blue', 'Green', 'Yellow', 'Red'], []]
costs = {0: 4, 1: 3, 2: 2, 3: 4, 4: 2, 5: 5}
print(bfs(stacks, costs))
