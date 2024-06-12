
from collections import deque

def sort_it(tubes):
    colors = {'Red': 0, 'Blue': 1, 'Green': 2}
    tubes = [[colors[ball] for ball in tube] for tube in tubes]
    queue = deque([(tubes, [])])
    visited = {tuple(tubes): []}
    while queue:
        current_tubes, current_moves = queue.popleft()
        if all(len(set(tube)) == 1 for tube in current_tubes):
            return current_moves
        for i in range(3):
            for j in range(3):
                if i != j and len(current_tubes[i]) > 0 and len(current_tubes[j]) < 8:
                    new_tubes = [list(tube) for tube in current_tubes]
                    ball = new_tubes[i].pop()
                    new_tubes[j].append(ball)
                    new_tubes = tuple(tuple(tube) for tube in new_tubes)
                    if new_tubes not in visited:
                        queue.append((new_tubes, current_moves + [(i, j)]))
                        visited[new_tubes] = []
    return []

tubes = [['Red', 'Red', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red', 'Red'], ['Blue', 'Blue', 'Green', 'Green', 'Blue']]
print(sort_it(tubes))
