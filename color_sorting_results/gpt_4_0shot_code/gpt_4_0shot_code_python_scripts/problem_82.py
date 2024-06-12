
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = tuple(sorted(start, key=lambda x: x[0] if x else ''))
    visited = {start}
    queue = deque([([start], [])])
    while queue:
        path, moves = queue.popleft()
        current = path[-1]
        if current == goal:
            return moves
        for i, tube in enumerate(current):
            if tube:
                for j in range(len(current)):
                    if i != j and (not current[j] or current[j][0] == tube[0] or len(current[j]) < 9):
                        new_tubes = list(map(list, current))
                        new_tubes[j].append(new_tubes[i].pop())
                        new_state = tuple(map(tuple, new_tubes))
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((path + [new_state], moves + [(i, j)]))

tubes = [['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'], ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
