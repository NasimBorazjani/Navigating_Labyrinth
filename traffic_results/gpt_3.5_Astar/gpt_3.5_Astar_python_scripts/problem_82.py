
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((15, 19, 13, 4, 'x', 'x', 13, 7, 16, 6, 'x', 'x', 17, 'x'),
                     (2, 2, 'x', 7, 'x', 12, 12, 'x', 19, 'x', 10, 4, 14, 2),
                     (11, 'x', 'x', 3, 7, 'x', 7, 'x', 'x', 6, 'x', 19, 'x', 1),
                     ('x', 'x', 11, 'x', 3, 'x', 17, 'x', 1, 20, 17, 8, 15, 1),
                     ('x', 'x', 13, 'x', 12, 17, 5, 4, 'x', 16, 9, 'x', 19, 14),
                     ('x', 16, 'x', 'x', 13, 17, 14, 6, 2, 17, 19, 6, 13, 6),
                     ('x', 1, 'x', 'x', 3, 10, 2, 18, 7, 8, 'x', 8, 'x', 'x'),
                     (12, 2, 1, 6, 11, 7, 10, 'x', 'x', 'x', 4, 2, 8, 'x'),
                     ('x', 'x', 'x', 13, 16, 2, 'x', 6, 9, 2, 11, 7, 14, 6),
                     ('x', 'x', 'x', 'x', 'x', 11, 'x', 16, 'x', 'x', 'x', 'x', 'x', 3),
                     ('x', 'x', 'x', 'x', 10, 'x', 3, 'x', 18, 9, 'x', 'x', 'x', 15),
                     ('x', 'x', 11, 9, 3, 'x', 'x', 16, 'x', 5, 'x', 4, 10, 'x'),
                     (18, 1, 13, 'x', 7, 'x', 7, 5, 'x', 11, 10, 2, 'x', 2),
                     ('x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 10, 'x', 'x', 14, 6))
    
    num_rows = 14
    num_cols = 14
    districts = {1: (0, 1), 2: (2, 6), 3: (7, 13)}
    start = (1, 13)
    end = (7, 4)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [], start)]
    
    while queue:
        _, g, actions, current = heapq.heappop(queue)
        
        if current == end:
            return actions
        
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_cost = g + initial_state[new_row][new_col]
                
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))
    
    return None

def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # Additionally, the heuristic ensures that Ben visits at least one workshop in each district
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    
    # Check if Ben has visited at least one workshop in each district
    for district, (start_row, end_row) in districts.items():
        if start_row <= current[0] <= end_row:
            h -= 1
    
    return h

print(a_star())
