
from queue import PriorityQueue

def manhattan_distance(char, target_pos):
    char_pos = (char // len(board[0]), char % len(board[0]))
    return abs(char_pos[0] - target_pos[0]) + abs(char_pos[1] - target_pos[1])

def heuristic(board):
    total_distance = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            char = board[i][j]
            if char != '_':
                target_pos = (i, target_words[i].index(char))
                total_distance += manhattan_distance(i * len(board[0]) + j, target_pos)
    return total_distance

def get_blank_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def get_neighbors(board):
    neighbors = []
    blank_pos = get_blank_position(board)
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_x, new_y = blank_pos[0] + dx, blank_pos[1] + dy
        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
            new_board = [list(row) for row in board]
            new_board[blank_pos[0]][blank_pos[1]], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[blank_pos[0]][blank_pos[1]]
            neighbors.append((new_board, (dx, dy)))
    return neighbors

def a_star(board):
    frontier = PriorityQueue()
    frontier.put((heuristic(board), board, []))
    visited = set()

    while not frontier.empty():
        _, current_board, actions = frontier.get()
        if current_board == target_words:
            return actions
        visited.add(tuple(tuple(row) for row in current_board))

        for neighbor, action in get_neighbors(current_board):
            if tuple(tuple(row) for row in neighbor) not in visited:
                new_actions = actions + [action]
                frontier.put((heuristic(neighbor) + len(new_actions), neighbor, new_actions))

    return None

target_words = [['s', 'i', 'e', 'n', 'a'], ['l', 'o', 'c', 'k', 'e', 'd'], ['c', 'o', 'n', 'c', 'h', 'e'], ['c', 'e', 'l', 't', 'i', 'c'], ['b', 'l', 'a', 'n', 'c', 'o']]
initial_board = [['o', 's', 'n', 'e', 'd', 'a'], ['l', 'k', 'c', 'c', 'e', 'h'], ['t', 'o', '_', 'c', 'n', 'e'], ['c', 'i', 'l', 'a', 'i', 'c'], ['b', 'l', 'e', 'n', 'c', 'o']]

board = [list(row) for row in initial_board]
actions = a_star(board)

print(actions)
