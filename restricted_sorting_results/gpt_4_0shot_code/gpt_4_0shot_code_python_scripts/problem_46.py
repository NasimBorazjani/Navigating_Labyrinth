
from collections import deque

def bfs(start, goal, cost):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state, action in neighbors(state, cost):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)
    return []

def neighbors(state, cost):
    result = []
    for i, stack in enumerate(state):
        if stack:
            block = stack[-1]
            for j, next_stack in enumerate(state):
                if i != j and (not next_stack or next_stack[-1] == block) and len(next_stack) < 5:
                    next_state = state[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = next_stack + [block]
                    action = (i, j)
                    result.append((next_state, action))
    result.sort(key=lambda x: cost[x[1][1]])
    return result

def solve(stacks):
    cost = {0: 2, 1: 1, 2: 6, 3: 3, 4: 1, 5: 5, 6: 4, 7: 2}
    start = [list(reversed(stack)) for stack in stacks]
    goal = [['Yellow']*4, ['Black']*4, ['Green']*4, ['Red']*4, ['Blue']*4, [], [], []]
    return bfs(start, goal, cost)

stacks = [[], [], [], ['Yellow', 'Black', 'Yellow', 'Black', 'Green'], ['Red', 'Yellow', 'Blue', 'Black', 'Black'], [], ['Red', 'Blue', 'Green', 'Red', 'Blue'], ['Green', 'Blue', 'Red', 'Yellow', 'Green']]
print(solve(stacks))
