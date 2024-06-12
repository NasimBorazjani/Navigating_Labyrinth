
from collections import deque

def move(tubes, move):
    from_tube, to_tube = move
    if not tubes[from_tube] or len(tubes[to_tube]) == 9:
        return None
    new_tubes = [tube.copy() for tube in tubes]
    ball = new_tubes[from_tube].pop()
    new_tubes[to_tube].append(ball)
    return new_tubes

def is_sorted(tubes):
    return all(len(set(tube)) == 1 for tube in tubes)

def sort_it(tubes):
    queue = deque([([], tubes)])
    while queue:
        path, tubes = queue.popleft()
        if is_sorted(tubes):
            return path
        for i in range(3):
            for j in range(3):
                if i != j:
                    move = (i, j)
                    new_tubes = move(tubes, move)
                    if new_tubes is not None:
                        queue.append((path + [move], new_tubes))

# Example usage:
initial_tubes = [['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue'],
                 ['Blue', 'Blue', 'Red', 'Blue', 'Green', 'Red'],
                 ['Green', 'Red', 'Green', 'Blue', 'Green', 'Red']]
print(sort_it(initial_tubes))
