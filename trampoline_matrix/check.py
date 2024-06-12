
def is_feasible(matrix, num_req_diag_moves, path, called_from_correct=False):
    # Define the possible moves from a cell
    if type(matrix) == str:
        matrix = eval(matrix)
    moves = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]
    diag_moves = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    num_diag_moves_taken = 0
    
    for i in range(len(path) - 1):
        if len(path[i]) != 2 or len(path[i + 1]) != 2:
            if called_from_correct:
                return False, None
            return False
        
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        
        # Check if the coordinates are within the matrix and contain 0
        if not (0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0]) and matrix[x1][y1] == 0):
            if called_from_correct:
                return False, None
            return False
        
        # Check if the next coordinate is a neighbour
        if not any((x1 + dx == x2 and y1 + dy == y2) for dx, dy in moves):
            if called_from_correct:
                return False, None
            return False
        
        if any((x1 + dx == x2 and y1 + dy == y2) for dx, dy in diag_moves):
            num_diag_moves_taken += 1
        
    # Check the last coordinate
    x, y = path[-1]
    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0):
        if called_from_correct:
            return False, None
        return False
    
    if called_from_correct:
        return True, num_diag_moves_taken
    return True


def is_correct(matrix, start, dest, num_req_diag_moves, path):
    
    if type(matrix) == str:
        matrix = eval(matrix)
        
    feasible, num_diag_moves_taken = is_feasible(matrix, num_req_diag_moves, path, called_from_correct = True)
    
    if num_diag_moves_taken != num_req_diag_moves:
        return False, None
    
    x_first, y_first = path[0]
    x_last, y_last = path[-1]
    if (feasible and 
        x_last == dest[0] and y_last == dest[1] 
        and x_first == start[0] and y_first == start[1]):
        return True, len(path)
    
    return False, None
    
  
