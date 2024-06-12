
from collections import deque

def bfs(start):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for next_state, action in successors(state):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)

def is_goal(tubes):
    return all(len(set(tube)) <= 1 for tube in tubes)

def successors(state):
    for i, src in enumerate(state):
        if src:
            for j, dst in enumerate(state):
                if i != j and (not dst or dst[-1] == src[-1] and len(dst) < 7):
                    next_state = state[:]
                    next_state[i] = src[:-1]
                    next_state[j] = dst + [src[-1]]
                    yield next_state, (i, j)

tubes = [['Red', 'Red', 'Red', 'Green'], ['Blue', 'Green', 'Green', 'Blue'], ['Blue', 'Red', 'Green', 'Blue']]
print(bfs(tubes))
