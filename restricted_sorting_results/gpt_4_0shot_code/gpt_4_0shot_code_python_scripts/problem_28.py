
from collections import deque
from copy import deepcopy

def bfs(stacks, costs):
    queue = deque([(stacks, [], 0)])
    visited = set()
    while queue:
        stacks, moves, cost = queue.popleft()
        if str(stacks) in visited:
            continue
        visited.add(str(stacks))
        if is_sorted(stacks):
            return moves
        for i in range(6):
            if not stacks[i]:
                continue
            for j in range(6):
                if i == j or len(stacks[j]) == 4:
                    continue
                if not stacks[j] or stacks[j][-1] == stacks[i][-1]:
                    new_stacks = deepcopy(stacks)
                    block = new_stacks[i].pop()
                    new_stacks[j].append(block)
                    new_moves = moves + [(i, j)]
                    new_cost = cost + costs[j]
                    queue.append((new_stacks, new_moves, new_cost))
    return []

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [['Green', 'Yellow', 'Red', 'Red'], [], ['Yellow', 'Green', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Green', 'Blue']]
costs = {0: 3, 1: 7, 2: 7, 3: 7, 4: 2, 5: 4}
print(bfs(stacks, costs))
