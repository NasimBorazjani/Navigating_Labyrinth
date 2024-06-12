def has_correct_type(solution):
    #the solution must be a list of coord tuples based on the instructions
    problem_node_type = tuple
    if (solution and type(solution) is list and 
        all(isinstance(item, problem_node_type) for item in solution)):
        return True
    return False

def is_feasible(matrix, solution):
    if not has_correct_type(solution):
        return False
    
    # Define the possible moves from a cell
    moves = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]
    
    for i in range(len(solution) - 1):
        x1, y1 = solution[i]
        x2, y2 = solution[i + 1]
        
        # Check if the coordinates are within the matrix and contain 0
        if not (0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0]) and matrix[x1][y1] == 0):
            return False
        
                # Check if the next coordinate is a neighbour
        if not any((x1 + dx == x2 and y1 + dy == y2) for dx, dy in moves):
            return False
    
    # Check the last coordinate
    x, y = solution[-1]
    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0):
        return False
    
    return True


def has_correct_start_coord(start, solution):
    if solution[0] == start:
        return True
    return False
    
    
def has_correct_dest_coord(dest, solution):
    if solution[-1] == dest:
        return True
    return False
    
# the parameters of the check_unitests function must be matrix, start, dest, solution based on the instructions     
def check_unitests(matrix, start, dest, solution):
    error_message = None
    #checking the unitests from the most basic one 
    if not has_correct_type(solution):
        error_message = """The answer returned by the code generated does not have the correct type. 
        Based on the instructions, the solution should be a list of coordinate tuples in Python sytax."""
        return False, error_message
    if not is_feasible(matrix, solution):
        error_message = """The code generated is returning an infeasible answer. This indicates
        that at least one of the actions taken in the solution is not adhering to the problem's defined rules."""
        return False, error_message
    if not has_correct_start_coord(start, solution):
        error_message = """The code generated is returning an incorrect answer. The actions reported in the 
        solution adhere to the rules defined in the problem; however,the solution does not have the correct 
        start coordinate, indicating the starting position of Alex in the trampoline matrix."""
        return False, error_message
    if not has_correct_dest_coord(dest, solution):
        error_message = """The code generated is returning an incorrect answer. The actions reported in the 
        solution adhere to the rules defined in the problem; however,the solution does not have the correct 
        destination coordinate, indicating the position of the trampoline Alex wants to reach"""
        return False, error_message
    return True, None