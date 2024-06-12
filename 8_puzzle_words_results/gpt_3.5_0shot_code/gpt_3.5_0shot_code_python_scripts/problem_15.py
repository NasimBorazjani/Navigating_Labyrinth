
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
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0] - 1][blank_pos[1]]
        new_board[blank_pos[0] - 1][blank_pos[1]] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-left'))
    if blank_pos[0] < len(board) - 1:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0] + 1][blank_pos[1]]
        new_board[blank_pos[0] + 1][blank_pos[1]] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'down-left'))
    if blank_pos[1] > 0:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0]][blank_pos[1] - 1]
        new_board[blank_pos[0]][blank_pos[1] - 1] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-right'))
    if blank_pos[1] < len(board[0]) - 1:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0]][blank_pos[1] + 1]
        new_board[blank_pos[0]][blank_pos[1] + 1] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'down-right'))
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
        
        if heuristic(current_board, target_words) == 0:
            return path
        
        for neighbor, direction in get_neighbors(current_board):
            new_cost = len(path) + 1 + heuristic(neighbor, target_words)
            frontier.put((new_cost, neighbor, path + [direction]))
    
    return None

initial_board = (('a', 'r', '_', 'c'), ('h', 'a', 'v', 'e'), ('a', 'g', 's', 'd'), ('b', 'i', 't', 'z'))
target_words = ['ric', 'have', 'sgad', 'batz']

result = a_star(initial_board, target_words)
print(result)
