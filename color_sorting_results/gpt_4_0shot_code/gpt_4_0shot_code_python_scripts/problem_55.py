
from collections import deque

def sort_it(tubes):
    start = tuple(tuple(tube) for tube in tubes)
    goal = (tuple(sorted(tube)) for tube in start)
    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        state, moves = queue.popleft()
        if all(tube == goal_tube for tube, goal_tube in zip(state, goal)):
            return moves
        for i, tube in enumerate(state):
            if not tube:
                continue
            for j in range(len(state)):
                if i == j or len(state[j]) == 8:
                    continue
                new_state = list(list(t) for t in state)
                new_state[j].append(new_state[i].pop())
                new_state_tuple = tuple(tuple(t) for t in new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state_tuple, moves + [(i, j)]))

tubes = [['Green', 'Blue', 'Blue', 'Red', 'Red'], ['Green', 'Red', 'Blue', 'Green', 'Green'], ['Red', 'Green', 'Blue', 'Blue', 'Red']]
print(sort_it(tubes))
