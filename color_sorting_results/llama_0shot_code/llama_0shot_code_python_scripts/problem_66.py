
from collections import deque

def move_ball(tubes, from_tube, to_tube):
    # Remove a ball from the 'from_tube' and add it to the 'to_tube'
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)

def next_states(tubes):
    # Generate all possible next states
    states = []
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and len(tubes[i]) > 0 and len(tubes[j]) < 8:
                new_tubes = [list(tube) for tube in tubes]
                move_ball(new_tubes, i, j)
                states.append((new_tubes, (i, j)))
    return states

def sort_it(initial_tubes):
    final_tubes = [['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'], 
                   ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'], 
                   ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue']]

    queue = deque([(initial_tubes, [])])
    visited = set()

    while queue:
        tubes, moves = queue.popleft()
        if tubes in visited:
            continue
        visited.add(str(tubes))
        if tubes == final_tubes:
            return moves
        for next_tubes, move in next_states(tubes):
            new_moves = moves + [move]
            queue.append((next_tubes, new_moves))

    return None

initial_tubes = [['Red', 'Green', 'Blue', 'Green', 'Red'], 
                 ['Red', 'Blue', 'Blue', 'Green', 'Red'], 
                 ['Red', 'Blue', 'Green', 'Green', 'Blue']]

print(sort_it(initial_tubes))
