
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state, action in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)

def neighbors(state):
    result = []
    for i, stack in enumerate(state):
        if stack:
            block = stack[-1]
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == block) and len(target) < 5:
                    next_state = state[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = target + [block]
                    action = (i, j)
                    result.append((next_state, action))
    return result

def solve(stacks):
    start = [list(reversed(stack)) for stack in stacks]
    goal = [sorted(stack) for stack in start]
    return bfs(start, goal)

stacks = [[], [], ['Green', 'Yellow', 'Black', 'Red', 'Black'], ['Black', 'Red', 'Yellow', 'Blue', 'Yellow'], ['Green', 'Blue', 'Blue', 'Red', 'Black'], [], [], ['Red', 'Green', 'Blue', 'Green', 'Yellow']]
print(solve(stacks))
