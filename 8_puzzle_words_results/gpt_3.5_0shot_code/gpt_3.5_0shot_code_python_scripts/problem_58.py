
from queue import PriorityQueue

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(board, target_words):
    total_distance = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char != '_':
                target_pos = [(i, k) for k, c in enumerate(target_words[i]) if c == char][0]
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
        neighbors.append(tuple(tuple(row) for row in new_board))
    if i > 0 and j < len(board[0]) - 1:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i-1][j+1] = new_board[i-1][j+1], new_board[i][j]
        neighbors.append(tuple(tuple(row) for row in new_board))
    if i < len(board) - 1 and j > 0:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i+1][j-1] = new_board[i+1][j-1], new_board[i][j]
        neighbors.append(tuple(tuple(row) for row in new_board))
    if i < len(board) - 1 and j < len(board[0]) - 1:
        new_board = [list(row) for row in board]
        new_board[i][j], new_board[i+1][j+1] = new_board[i+1][j+1], new_board[i][j]
        neighbors.append(tuple(tuple(row) for row in new_board))
    return neighbors

def a_star(initial_board, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_board))
    came_from = {}
    cost_so_far = {initial_board: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == tuple(tuple(row) for row in target_words):
            break

        for next_board in get_neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next_board not in cost_so_far or new_cost < cost_so_far[next_board]:
                cost_so_far[next_board] = new_cost
                priority = new_cost + heuristic(next_board, target_words)
                frontier.put((priority, next_board))
                came_from[next_board] = current

    actions = []
    while current != initial_board:
        prev_board = came_from[current]
        i, j = get_blank_position(current)
        prev_i, prev_j = get_blank_position(prev_board)
        if i < prev_i and j < prev_j:
            actions.append("down-right")
        elif i < prev_i and j > prev_j:
            actions.append("down-left")
        elif i > prev_i and j < prev_j:
            actions.append("up-right")
        elif i > prev_i and j > prev_j:
            actions.append("up-left")
        current = prev_board

    return actions[::-1]

initial_board = [['i', 'e', 'e', 'd'], ['v', 't', 'n', 'l'], ['o', 'd', '_', 'a'], ['p', 'r', 'c', 'e'], ['p', 'i', 'o', 'l']]
target_words = [['e', 'l', 'd', '_'], ['v', 'i', 'n', 't'], ['e', 'd', 'e', 'a'], ['p', 'o', 'c', 'o'], ['p', 'i', 'r', 'l']]

actions = a_star(tuple(tuple(row) for row in initial_board), target_words)
print(actions)
