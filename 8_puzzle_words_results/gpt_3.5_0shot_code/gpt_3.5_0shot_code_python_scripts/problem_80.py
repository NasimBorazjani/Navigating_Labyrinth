
from queue import PriorityQueue

def manhattan_distance(char, target_pos):
    char_pos = (char[0], char.index('_'))
    return abs(char_pos[0] - target_pos[0]) + abs(char_pos[1] - target_pos[1])

def heuristic(board, target_words):
    total_distance = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char != '_':
                target_pos = (i, target_words[i].index(char))
                total_distance += manhattan_distance(char, target_pos)
    return total_distance

def get_neighbors(board):
    neighbors = []
    blank_pos = None
    for i, row in enumerate(board):
        if '_' in row:
            blank_pos = (i, row.index('_'))
            break
    if blank_pos[0] > 0:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0]-1][blank_pos[1]]
        new_board[blank_pos[0]-1][blank_pos[1]] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-left'))
    if blank_pos[0] < len(board)-1:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0]+1][blank_pos[1]]
        new_board[blank_pos[0]+1][blank_pos[1]] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'down-left'))
    if blank_pos[1] > 0:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0]][blank_pos[1]-1]
        new_board[blank_pos[0]][blank_pos[1]-1] = '_'
        neighbors.append((tuple(tuple(row) for row in new_board), 'up-right'))
    if blank_pos[1] < len(board[0])-1:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]] = new_board[blank_pos[0]][blank_pos[1]+1]
        new_board[blank_pos[0]][blank_pos[1]+1] = '_'
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
        
        if all(''.join(row) == word for row, word in zip(current_board, target_words)):
            return path
        
        for neighbor, direction in get_neighbors(current_board):
            new_path = path + [direction]
            priority = len(new_path) + heuristic(neighbor, target_words)
            frontier.put((priority, neighbor, new_path))
    
    return None

initial_board = [['d', 'w', 'p', 'l', 't'], ['e', 'i', 'd', 'e', 'c'], ['_', 'q', 'e', 'i', 'r'], ['m', 'e', 'c', 'u', 'r'], ['y', 'u', 'a', 't', 'a']]
target_words = ['welt', 'eddic', 'equip', 'macer', 'yurta']

result = a_star(tuple(tuple(row) for row in initial_board), target_words)
print(result)
