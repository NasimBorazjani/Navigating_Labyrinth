
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_tile_pos(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return (i, j)

def get_possible_moves(pos):
    possible_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x, y = pos
    return [(dx, dy) for dx, dy in possible_moves if 0 <= x + dx < 3 and 0 <= y + dy < 3]

def swap(state, pos_a, pos_b):
    state = [list(row) for row in state]
    state[pos_a[0]][pos_a[1]], state[pos_b[0]][pos_b[1]] = state[pos_b[0]][pos_b[1]], state[pos_a[0]][pos_a[1]]
    return tuple(tuple(row) for row in state)

def solve_puzzle(initial_state):
    goal_state = ((82, 80, 76), (73, 67, 62), (47, 24, '_'))
    queue = PriorityQueue()
    queue.put((0, initial_state, []))
    visited = set()

    while not queue.empty():
        _, current_state, path = queue.get()
        visited.add(current_state)

        if current_state == goal_state:
            return path

        empty_pos = get_tile_pos(current_state, '_')
        for dx, dy in get_possible_moves(empty_pos):
            neighbor = (empty_pos[0] + dx, empty_pos[1] + dy)
            neighbor_state = swap(current_state, empty_pos, neighbor)
            if neighbor_state not in visited:
                queue.put((heuristic(neighbor, get_tile_pos(goal_state, '_')), neighbor_state, path + [current_state[neighbor[0]][neighbor[1]]]))

initial_state = ((80, 62, 76), (47, 67, 82), (24, 73, '_'))
print(solve_puzzle(initial_state))
