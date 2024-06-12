
from collections import deque

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
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())
                    new_moves = list(moves)
                    new_moves.append((i, j))
                    new_cost = cost + costs[j]
                    queue.append((new_stacks, new_moves, new_cost))
    return []

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [[], ['Green', 'Red', 'Yellow', 'Blue'], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Red', 'Yellow', 'Blue', 'Green'], []]
costs = {0: 4, 1: 2, 2: 5, 3: 2, 4: 4, 5: 1}
print(bfs(stacks, costs))
