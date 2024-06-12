
from queue import PriorityQueue

def heuristic(board, target_words):
    total_cost = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '_' and board[i][j] != target_words[i][j]:
                total_cost += 1
    return total_cost

def get_neighbors(board):
    neighbors = []
    blank_pos = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == '_'][0]
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        new_x, new_y = blank_pos[0] + dx, blank_pos[1] + dy
        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
            new_board = [list(row) for row in board]
            new_board[blank_pos[0]][blank_pos[1]], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[blank_pos[0]][blank_pos[1]]
            neighbors.append((new_board, (dx, dy)))
    return neighbors

def a_star(board, target_words):
    pq = PriorityQueue()
    pq.put((0, board, []))
    visited = set()
    
    while not pq.empty():
        cost, current_board, actions = pq.get()
        
        if current_board == target_words:
            return actions
        
        if str(current_board) in visited:
            continue
        
        visited.add(str(current_board))
        
        for neighbor, action in get_neighbors(current_board):
            new_cost = len(actions) + heuristic(neighbor, target_words)
            pq.put((new_cost, neighbor, actions + [action]))
    
    return None

target_words = [['g', 'o', 'n', 'g', '_'], ['c', 'l', 'o', 'w', 'n'], ['b', 'r', 'e', 'n', 't'], ['d', 'e', 'w', 'a', 'x'], ['t', 'h', 'o', 'r', 'p']]
initial_board = [['l', 'g', 'a', 'n', 'g'], ['c', 'o', 'o', 'e', 'n'], ['e', 'r', '_', 'n', 't'], ['d', 'b', 'w', 'o', 'x'], ['t', 'h', 'w', 'r', 'p']]

actions = a_star(initial_board, target_words)
print(actions)
