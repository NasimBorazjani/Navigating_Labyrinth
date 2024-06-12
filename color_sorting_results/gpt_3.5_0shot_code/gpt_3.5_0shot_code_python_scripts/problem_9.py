
from collections import deque

def is_sorted(tubes):
    return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)

def get_neighbors(tubes):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if i != j and len(tubes[j]) < 6 and (not tubes[i] or tubes[i][0] == tubes[j][0]):
                new_tubes = [list(tube) for tube in tubes]
                new_tubes[j].insert(0, new_tubes[i].pop(0))
                neighbors.append((i, j, new_tubes))
    return neighbors

def solve(tubes):
    queue = deque([(0, [], tubes)])
    
    while queue:
        i, moves, current_tubes = queue.popleft()
        
        if is_sorted(current_tubes):
            return moves
        
        for move in get_neighbors(current_tubes):
            if move[2] not in [state for _, _, state in queue]:
                queue.append((move[1], moves + [(move[0], move[1])], move[2])

initial_state = [['Green', 'Blue', 'Green', 'Red'], ['Red', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]
solution = solve(initial_state)
print(solution)
