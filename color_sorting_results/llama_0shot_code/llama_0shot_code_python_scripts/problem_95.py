
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

# Test the function with the given initial state of the tubes
initial_tubes = [
    ['Green', 'Green', 'Green', 'Red', 'Blue', 'Blue'],
    ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'],
    ['Blue', 'Green', 'Blue', 'Red', 'Red', 'Blue']
]

print(sort_it(initial_tubes))
