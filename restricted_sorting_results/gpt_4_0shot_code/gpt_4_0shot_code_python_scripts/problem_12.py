
from collections import deque

def solve(stacks):
    costs = {tuple(map(tuple, stacks)): 0}
    prev = {tuple(map(tuple, stacks)): None}
    q = deque([stacks])

    while q:
        stacks = q.popleft()
        if all(len(set(stack)) <= 1 for stack in stacks):
            break

        for i in range(6):
            if not stacks[i]:
                continue

            for j in range(6):
                if i == j or len(stacks[j]) == 4 or (stacks[j] and stacks[j][-1] != stacks[i][-1]):
                    continue

                new_stacks = [list(stack) for stack in stacks]
                new_stacks[j].append(new_stacks[i].pop())
                new_stacks = tuple(map(tuple, new_stacks))

                cost = costs[tuple(map(tuple, stacks))] + {0: 2, 1: 2, 2: 3, 3: 7, 4: 1, 5: 7}[j]
                if new_stacks not in costs or cost < costs[new_stacks]:
                    costs[new_stacks] = cost
                    prev[new_stacks] = (tuple(map(tuple, stacks)), i, j)
                    q.append(new_stacks)

    transfers = []
    while prev[stacks]:
        stacks, i, j = prev[stacks]
        transfers.append((i, j))
    return transfers[::-1]

stacks = [['Green', 'Yellow', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Yellow'], [], [], ['Blue', 'Red', 'Blue', 'Green'], []]
print(solve(stacks))
