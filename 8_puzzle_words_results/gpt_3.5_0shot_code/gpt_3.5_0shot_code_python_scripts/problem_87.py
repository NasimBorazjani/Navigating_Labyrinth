
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(board, target_words):
    total_distance = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '_':
                target_row = target_words.index(board[i][j])
                target_pos = (i, target_row)
                total_distance += manhattan_distance((i, j), target_pos)
    return total_distance

def get_neighbors(board):
    neighbors = []
    blank_pos = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                blank_pos = (i, j)
                break
    if blank_pos[0] > 0:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]], new_board[blank_pos[0]-1][blank_pos[1]+1] = new_board[blank_pos[0]-1][blank_pos[1]+1], new_board[blank_pos[0]][blank_pos[1]]
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-right'))
    # Add other neighbor directions (down-right, up-left, down-left) in a similar way
    return neighbors

def a_star(initial_board, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_board, []))
    visited = set()

    while not frontier.empty():
        cost, current_board, path = frontier.get()
        if current_board in visited:
            continue
        visited.add(current_board)

        if current_board == tuple(tuple(row) for row in target_words):
            return path

        for neighbor, direction in get_neighbors(current_board):
            new_cost = len(path) + 1 + heuristic(neighbor, target_words)
            frontier.put((new_cost, neighbor, path + [direction]))

    return None

initial_board = [['e', 'e', 'l', 'h', 'o'], ['m', 'r', 't', 'u', 'n'], ['p', 'e', '_', 'c', 'i'], ['t', 'c', 'l', 'h', 'p'], ['m', 'u', 'i', 'g', 'a']]
target_words = [['e', 'c', 'h', 'o', '_'], ['m', 'e', 't', 'i', 'n'], ['p', 'e', 'r', 'c', 'h'], ['t', 'u', 'l', 'i', 'p'], ['m', 'u', 'l', 'g', 'a']]

result = a_star(tuple(tuple(row) for row in initial_board), target_words)
print(result)
