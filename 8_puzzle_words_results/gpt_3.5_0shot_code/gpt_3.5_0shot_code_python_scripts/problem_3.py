
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
    for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_i, new_j = blank_pos[0] + di, blank_pos[1] + dj
        if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
            new_board = [list(row) for row in board]
            new_board[blank_pos[0]][blank_pos[1]], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[blank_pos[0]][blank_pos[1]]
            neighbors.append((tuple(tuple(row) for row in new_board), (di, dj)))
    return neighbors

def a_star(initial_board, target_words):
    pq = PriorityQueue()
    pq.put((heuristic(initial_board, target_words), 0, initial_board, []))
    visited = set()
    
    while not pq.empty():
        _, cost, board, path = pq.get()
        
        if board in visited:
            continue
        
        visited.add(board)
        
        if all(''.join(row) == word for row, word in zip(board, target_words)):
            return path
        
        for neighbor, move in get_neighbors(board):
            new_cost = cost + 1
            new_path = path + [move]
            pq.put((new_cost + heuristic(neighbor, target_words), new_cost, neighbor, new_path))
    
    return None

initial_board = [['v', 't', 'u', 'i'], ['o', 'w', 'e', 'i'], ['y', 'd', '_', 'c'], ['d', 'i', 'e', 'm']]
target_words = ['twi', 'ovey', 'udic', 'diem']

result = a_star(tuple(tuple(row) for row in initial_board), target_words)
print(result)
