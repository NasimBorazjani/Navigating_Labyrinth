
from collections import deque

def perform_move(tubes, move):
    tube_from, tube_to = move
    ball = tubes[tube_from].pop()
    tubes[tube_to].append(ball)
    return tubes

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def sort_it(tubes):
    initial_tubes = [list(tube) for tube in tubes]
    queue = deque([(initial_tubes, [])])
    visited = set()

    while queue:
        current_tubes, moves = queue.popleft()
        state = tuple(tuple(tube) for tube in current_tubes)

        if state in visited:
            continue
        visited.add(state)

        if is_sorted(current_tubes):
            return moves

        for tube_from in range(3):
            for tube_to in range(3):
                if tube_from != tube_to and len(current_tubes[tube_to]) < 8:
                    new_tubes = perform_move(list(current_tubes), (tube_from, tube_to))
                    queue.append((new_tubes, moves + [(tube_from, tube_to)]))

    return None

tubes = [['Red', 'Red', 'Blue', 'Blue', 'Red'], 
         ['Green', 'Green', 'Red', 'Red', 'Green'], 
         ['Blue', 'Blue', 'Green', 'Blue', 'Green']]

print(sort_it(tubes))
