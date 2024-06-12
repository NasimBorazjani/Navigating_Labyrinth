
from collections import deque

def restricted_sorting(stacks):
    costs = {0: 2, 1: 6, 2: 5, 3: 2, 4: 5, 5: 7}
    visited = set()
    queue = deque([("", stacks)])
    while queue:
        path, stacks = queue.popleft()
        if str(stacks) in visited:
            continue
        visited.add(str(stacks))
        if all(len(set(stack)) <= 1 for stack in stacks):
            return [(int(step[0]), int(step[1])) for step in path.split(",") if step]
        for i in range(6):
            if not stacks[i]:
                continue
            for j in range(6):
                if i == j or len(stacks[j]) == 4 or (stacks[j] and stacks[j][-1] != stacks[i][-1]):
                    continue
                new_stacks = [list(stack) for stack in stacks]
                new_stacks[j].append(new_stacks[i].pop())
                queue.append((path + "," + str(i) + str(j), new_stacks))
    return []

stacks = [['Red', 'Green', 'Yellow', 'Blue'], [], ['Yellow', 'Green', 'Blue', 'Red'], [], ['Green', 'Red', 'Blue', 'Yellow'], []]
print(restricted_sorting(stacks))
