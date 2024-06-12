
from collections import deque

def sort_it(tubes):
    colors = ['Red', 'Blue', 'Green']
    final_states = [['R', 'R', 'B', 'B'], ['B', 'B', 'R', 'R'], ['G', 'G', 'R', 'R']]
    visited = set()
    queue = deque([(tubes, [])])
    while queue:
        tubes, moves = queue.popleft()
        state = ''.join(colors[tubes[i][j]] for i in range(3) for j in range(4))
        if state in final_states:
            return moves
        for i in range(3):
            for j in range(4):
                for k in range(3):
                    if k != i and len(tubes[k]) < 7:
                        new_tubes = [list(tube) for tube in tubes]
                        ball = new_tubes[i].pop(j)
                        new_tubes[k].append(ball)
                        new_state = tuple(''.join(''.join(tube) for tube in new_tubes))
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_tubes, moves + [(i, j, k)]))

initial_tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Green', 'Green', 'Blue', 'Blue'], ['Green', 'Green', 'Red', 'Red']]
print(sort_it(initial_tubes))
