
from collections import deque

def move_ball(tubes, from_tube, to_tube):
    # Move the ball from the 'from_tube' to the 'to_tube'
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)
    return tubes

def is_sorted(tubes):
    # Check if the tubes are sorted
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def bfs(tubes):
    queue = deque([(tubes, [])])
    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if j != i and len(tubes[j]) < 9:
                    new_tubes = move_ball(list(map(list, tubes)), i, j)
                    queue.append((new_tubes, moves + [(i, j)]))

initial_tubes = [['Blue', 'Green', 'Red', 'Red', 'Blue', 'Green'], 
                 ['Blue', 'Red', 'Green', 'Green', 'Green', 'Red'], 
                 ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Green']]

print(bfs(initial_tubes))
