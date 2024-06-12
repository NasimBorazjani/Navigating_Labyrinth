
from collections import deque

def bfs(start):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for next_state, move in get_moves(state):
            if next_state not in seen:
                queue.append((next_state, path + [move]))
                seen.add(next_state)

def is_goal(tubes):
    return all(len(set(tube)) <= 1 for tube in tubes)

def get_moves(tubes):
    for i, tube in enumerate(tubes):
        if tube:
            for j, other_tube in enumerate(tubes):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                    next_tubes = tubes[:]
                    next_tubes[i] = tube[:-1]
                    next_tubes[j] = other_tube + [tube[-1]]
                    yield next_tubes, (i, j)

start = [['Green', 'Blue', 'Green', 'Blue'], ['Red', 'Green', 'Red', 'Red'], ['Green', 'Blue', 'Red', 'Blue']]
print(bfs(start))
