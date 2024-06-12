
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
                if tuple(tuple(tube) for tube in new_state) not in visited:
                    visited.add(tuple(tuple(tube) for tube in new_state))
                    queue.append((new_state, moves + [(a, b)]))

tubes = [['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue'], ['Blue', 'Blue', 'Red', 'Blue', 'Green', 'Red'], ['Green', 'Red', 'Green', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
