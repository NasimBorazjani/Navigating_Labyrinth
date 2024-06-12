
from collections import deque
from copy import deepcopy

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def bfs(stacks, costs):
    queue = deque([(stacks, [], 0)])
    visited = set()
    while queue:
        stacks, path, cost = queue.popleft()
        if str(stacks) in visited:
            continue
        visited.add(str(stacks))
        if is_sorted(stacks):
            return path
        for i in range(6):
            if stacks[i]:
                for j in range(6):
                    if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 4:
                        new_stacks = deepcopy(stacks)
                        block = new_stacks[i].pop()
                        new_stacks[j].append(block)
                        new_path = path + [(i, j)]
                        new_cost = cost + costs[j]
                        queue.append((new_stacks, new_path, new_cost))
    return []

stacks = [['Red', 'Green', 'Green', 'Yellow'], [], ['Blue', 'Blue', 'Green', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Yellow'], []]
costs = {0: 4, 1: 1, 2: 7, 3: 3, 4: 2, 5: 2}
print(bfs(stacks, costs))
