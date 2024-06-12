
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(board, target_words):
    total_distance = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char != '_':
                target_pos = [(i, pos) for pos, word in enumerate(target_words) if char in word][0]
                total_distance += manhattan_distance((i, j), target_pos)
    return total_distance

def get_blank_position(board):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == '_':
                return (i, j)

def get_neighbors(board):
    i, j = get_blank_position(board)
    neighbors = []
    if i > 0 and j > 0:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i-1][j-1] = new_board[i-1][j-1], new_board[i][j]
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-left'))
    if i > 0 and j < len(board[0]) - 1:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i-1][j+1] = new_board[i-1][j+1], new_board[i][j]
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-right'))
    if i < len(board) - 1 and j > 0:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i+1][j-1] = new_board[i+1][j-1], new_board[i][j]
        neighbors.append((tuple(tuple(row) for row in new_board), 'down-left'))
    if i < len(board) - 1 and j < len(board[0]) - 1:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i+1][j+1] = new_board[i+1][j+1], new_board[i][j]
        neighbors.append((tuple(tuple(row) for row in new_board), 'down-right'))
    return neighbors

def a_star(initial_board, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_board, []))
    visited = set()

    while not frontier.empty():
        _, current_board, path = frontier.get()
        if current_board in visited:
            continue
        visited.add(current_board)

        if heuristic(current_board, target_words) == 0:
            return path

        for neighbor, direction in get_neighbors(current_board):
            new_path = path + [direction]
            priority = len(new_path) + heuristic(neighbor, target_words)
            frontier.put((priority, neighbor, new_path))

    return None

initial_board = [['u', 'n', 'a', 'b'], ['g', 'b', 'l', 'l'], ['a', 'o', '_', 'k'], ['t', 'o', 'l', 'c'], ['f', 'l', 'o', 'b']]
target_words = ['nab', 'gull', 'book', 'talc', 'flob']

result = a_star(tuple(tuple(row) for row in initial_board), target_words)
print(result)
