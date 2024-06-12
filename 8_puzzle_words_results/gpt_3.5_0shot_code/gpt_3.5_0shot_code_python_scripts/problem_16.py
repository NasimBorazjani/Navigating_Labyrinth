
from queue import PriorityQueue

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def heuristic(board, target_words):
    total_distance = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '_':
                target_row = target_words.index(board[i][j])
                target_pos = (i, target_row)
                total_distance += manhattan_distance((i, j), target_pos)
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
        new_pos = (blank_pos[0] + dx, blank_pos[1] + dy)
        if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]):
            new_board = [list(row) for row in board]
            new_board[blank_pos[0]][blank_pos[1]], new_board[new_pos[0]][new_pos[1]] = new_board[new_pos[0]][new_pos[1]], new_board[blank_pos[0]][blank_pos[1]]
            neighbors.append((tuple(row) for row in new_board))
    return neighbors

def a_star(initial_board, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_board))
    came_from = {initial_board: None}
    g_score = {initial_board: 0}
    
    while not frontier.empty():
        _, current = frontier.get()
        
        if all(current[i][i] == target_words[i] for i in range(len(target_words))):
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path[1:]
        
        for neighbor in get_neighbors(current):
            new_g_score = g_score[current] + 1
            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                g_score[neighbor] = new_g_score
                f_score = new_g_score + heuristic(neighbor, target_words)
                frontier.put((f_score, neighbor))
                came_from[neighbor] = current
    
    return None

initial_board = [('o', 'g', 'h', 'a'), ('y', 'c', 'd', 'l'), ('o', 'a', '_', 'l'), ('a', 'w', 'l', 'e')]
target_words = ['goa', 'yodh', 'wall', 'acle']

solution = a_star(tuple(tuple(row) for row in initial_board), target_words)

if solution:
    for i in range(len(solution) - 1):
        current_board = solution[i]
        next_board = solution[i + 1]
        blank_pos = get_blank_position(next_board)
        prev_blank_pos = get_blank_position(current_board)
        dx = blank_pos[0] - prev_blank_pos[0]
        dy = blank_pos[1] - prev_blank_pos[1]
        if dx == 1 and dy == 1:
            print("Swap down-right")
        elif dx == 1 and dy == -1:
            print("Swap down-left")
        elif dx == -1 and dy == 1:
            print("Swap up-right")
        elif dx == -1 and dy == -1:
            print("Swap up-left")
else:
    print("No solution found")
