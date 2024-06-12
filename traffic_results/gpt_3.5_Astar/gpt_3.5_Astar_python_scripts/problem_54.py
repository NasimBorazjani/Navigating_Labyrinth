
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((19, 14, 16, 4, 15, 16, 15, 'x', 9, 'x', 'x', 'x'),
                     ('x', 7, 12, 6, 'x', 12, 'x', 3, 'x', 14, 5, 9),
                     (1, 12, 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 10, 1),
                     ('x', 1, 15, 14, 'x', 2, 13, 'x', 'x', 'x', 10, 9),
                     (7, 'x', 13, 'x', 14, 1, 14, 8, 'x', 'x', 8, 5),
                     (18, 'x', 8, 13, 12, 13, 'x', 12, 3, 'x', 14, 'x'),
                     ('x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 17, 10),
                     ('x', 5, 'x', 4, 'x', 'x', 'x', 3, 5, 6, 6, 11),
                     ('x', 15, 6, 'x', 4, 18, 'x', 'x', 14, 10, 2, 8),
                     (13, 10, 13, 7, 3, 6, 'x', 'x', 10, 17, 10, 15),
                     (4, 'x', 'x', 7, 19, 4, 13, 13, 12, 'x', 'x', 13),
                     (5, 'x', 'x', 9, 19, 18, 'x', 'x', 16, 'x', 2, 'x'))
    
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 8), 3: (9, 11)}
    start = (4, 11)
    end = (9, 2)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(len(set(path).intersection(range(districts[i][0], districts[i][1]+1))) > 0 for i in districts):
            return path
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    h = heuristic((new_row, new_col), end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))
    
    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
