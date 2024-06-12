
from collections import deque
from itertools import permutations

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    target = [sorted(tube, reverse=True) for tube in tubes]
    visited = set()
    queue = deque([(tubes, [])])
    while queue:
        state, moves = queue.popleft()
        if all(state[i] == target[i] for i in range(3)):
            return moves
        for a, b in permutations(range(3), 2):
            if state[a] and (not state[b] or state[a][-1] == state[b][-1]) and len(state[b]) < 9:
                new_state = [tube.copy() for tube in state]
                new_state[b].append(new_state[a].pop())
                t = tuple(tuple(tube) for tube in new_state)
                if t not in visited:
                    visited.add(t)
                    queue.append((new_state, moves + [(a, b)]))

tubes = [['Green', 'Green', 'Red', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Blue', 'Blue', 'Red', 'Blue'], ['Blue', 'Green', 'Blue', 'Blue', 'Red', 'Green']]
print(sort_it(tubes))
