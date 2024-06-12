
from collections import deque
from itertools import permutations

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    target = sorted(tube for tube in tubes for _ in range(len(tube)))
    visited = set()
    queue = deque([(tubes, [])])
    while queue:
        tubes, moves = queue.popleft()
        if all(tube == target[i] for i, tube in enumerate(tubes)):
            return moves
        for i, j in permutations(range(len(tubes)), 2):
            if tubes[i] and (not tubes[j] or tubes[i][-1] == tubes[j][-1]) and len(tubes[j]) < 9:
                new_tubes = [tube.copy() for tube in tubes]
                new_tubes[j].append(new_tubes[i].pop())
                state = tuple(tuple(tube) for tube in new_tubes)
                if state not in visited:
                    visited.add(state)
                    queue.append((new_tubes, moves + [(i, j)]))

tubes = [['Blue', 'Red', 'Blue', 'Red', 'Blue', 'Red'], ['Blue', 'Blue', 'Red', 'Green', 'Green', 'Green'], ['Green', 'Red', 'Green', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
