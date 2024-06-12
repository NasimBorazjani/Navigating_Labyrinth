
    

#returns the path cost as well
def is_feasible(matrix, path, called_from_correct = False):
    path_cost = 0
    # Define the possible moves from a cell
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(len(path) - 1):
        if len(path[i]) != 2:
            if called_from_correct:    
                return False, None
            else:
                return False
            
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        
        # Check if the coordinates are within the matrix and contain 0
        if not (0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0])) or matrix[x1][y1] == 'x':
            if called_from_correct:    
                return False, None
            else:
                return False
        
        # Check if the next coordinate is a neighbour
        if not any((x1 + dx == x2 and y1 + dy == y2) for dx, dy in moves):
            if called_from_correct:    
                return False, None
            else:
                return False
        
        if i != 0:
            path_cost += int(matrix[x1][y1])
        

    x, y = path[-1]
    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])) or matrix[x][y] == 'x':
        if called_from_correct:    
            return False, None
        else:
            return False
    else:
        path_cost += int(matrix[x][y])
        
    
    if called_from_correct:    
        return True, path_cost
    else:
        return True


def is_correct(matrix, start, dest, district_1_last_row, district_2_last_row, path):
    feasible, path_cost = is_feasible(matrix, path, called_from_correct = True)
    
    x_first, y_first = path[0]
    x_last, y_last = path[-1]
    
    visited_d1 = False
    visited_d2 = False
    visited_d3 = False
    
    for current in path:
        if 0 <= current[0] <= district_1_last_row:
            visited_d1 = True
        elif district_1_last_row < current[0] <= district_2_last_row:
            visited_d2 = True
        elif district_2_last_row < current[0] <= len(matrix) - 1:
            visited_d3 = True
    if (feasible and x_last == dest[0] and y_last == dest[1] 
        and x_first == start[0] and y_first == start[1] and visited_d1
        and visited_d2 and visited_d3):
        return True , path_cost
    
    return False, None
    
    
    
"""matrix = [['11', 'x', '7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', '1', 'x', '15', 'x', 'x', 'x', 'x'], ['13', '9', '5', '19', '1', '15', '14', '11', '8', '9'], ['7', 'x', '8', '16', '5', '5', '19', '12', '15', '4'], ['16', 'x', '11', '5', '1', '13', '5', '7', '19', '7'], ['1', 'x', '9', 'x', '7', '10', '17', '9', 'x', '12'], ['8', 'x', 'x', '15', 'x', '16', '5', '5', '7', '9'], ['16', '19', '15', '15', '2', '4', '21', '20', '15', '12'], ['10', '2', '16', '3', '4', '11', '3', '9', '15', '13'], ['8', '19', '14', '3', '12', '3', '9', '14', '2', '21']]


start = (2, 7)
dest = (6,0)
path = [(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]

print(is_correct(matrix, start, dest, 1, 6, path))"""

"""city = [[19, 'x', 1, 'x', 2, 17, 'x', 'x', 'x'],
            ['x', 'x', 14, 'x', 11, 'x', 'x', 18, 'x'],
            [19, 'x', 19, 7, 'x', 6, 'x', 'x', 'x'],
            [6, 'x', 'x', 3, 'x', 8, 10, 'x', 16],
            [3, 7, 'x', 14, 'x', 10, 9, 6, 15],
            [13, 'x', 6, 1, 'x', 'x', 'x', 12, 14],
            ['x', 8, 5, 16, 14, 'x', 10, 5, 16],
            [18, 4, 9, 1, 11, 9, 9, 18, 13],
            ['x', 'x', 16, 13, 16, 'x', 17, 'x', 11]]

# Encoding other variables of the problem
num_rows = 9
num_cols = 9
initial_coordinate = (3, 8)
goal_coordinate = (6, 1)
district_1_last_row = 3
district_2_last_row = 5
path = [(3, 8), (4, 8), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1)]
print(is_correct(city, initial_coordinate, goal_coordinate,
                 district_1_last_row, district_2_last_row, path))"""
