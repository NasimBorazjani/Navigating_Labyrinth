
from collections import deque

def bfs(initial, target):
    queue = deque([(initial, [])])
    visited = set()
    while queue:
        state, swaps = queue.popleft()
        if state not in visited:
            visited.add(state)
            if state == target:
                return swaps
            for direction, new_state, swap in generate_next_states(state):
                queue.append((new_state, swaps + [swap]))

def generate_next_states(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                    newi, newj = i + di, j + dj
                    if 0 <= newi < len(state) and 0 <= newj < len(state[i]):
                        new_state = swap(state, i, j, newi, newj)
                        swap_direction = get_swap_direction((i, j), (newi, newj))
                        yield swap_direction, new_state, swap_direction

def swap(state, i1, j1, i2, j2):
    new_state = [list(row) for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return [''.join(row) for row in new_state]

def get_swap_direction(pos1, pos2):
    di, dj = pos2[0] - pos1[0], pos2[1] - pos1[1]
    if di == -1 and dj == 1:
        return 'up-right'
    elif di == 1 and dj == 1:
        return 'down-right'
    elif di == -1 and dj == -1:
        return 'up-left'
    elif di == 1 and dj == -1:
        return 'down-left'

initial = ['a', 's', '_', 'p', 'e'], ['c', 'u', 'd', 'o', 's'], ['l', 'u', 'u', 'a', 's'], ['r', 'c', 'u', 'n', 'e']
target = 'supe', 'cadus', 'nucal', 'rouse'

print(bfs(initial, target))
