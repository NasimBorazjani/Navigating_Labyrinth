
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((6, 6, 2, 'x', 13, 'x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 3, 'x'),
                     (6, 11, 'x', 14, 'x', 'x', 'x', 1, 5, 6, 1, 19, 2, 7, 14),
                     (16, 4, 12, 13, 17, 4, 'x', 'x', 'x', 14, 'x', 'x', 9, 9, 13),
                     ('x', 11, 6, 14, 'x', 16, 'x', 1, 10, 18, 11, 'x', 'x', 13, 'x'),
                     ('x', 'x', 14, 4, 19, 1, 2, 16, 15, 'x', 15, 'x', 'x', 'x', 'x'),
                     (13, 6, 16, 13, 5, 9, 'x', 6, 10, 3, 1, 14, 'x', 17, 'x'),
                     ('x', 'x', 19, 8, 'x', 2, 4, 'x', 'x', 4, 9, 13, 13, 11, 5),
                     ('x', 11, 17, 19, 11, 18, 'x', 8, 'x', 'x', 17, 17, 13, 9, 15),
                     (11, 4, 'x', 3, 3, 8, 5, 'x', 'x', 'x', 20, 19, 'x', 'x', 12),
                     (2, 'x', 'x', 'x', 'x', 16, 7, 13, 4, 'x', 7, 16, 'x', 5, 1),
                     (14, 9, 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 14, 20, 11, 16, 'x'),
                     (3, 'x', 1, 'x', 13, 'x', 9, 'x', 15, 19, 4, 'x', 'x', 2),
                     ('x', 8, 'x', 'x', 'x', 6, 'x', 16, 'x', 'x', 'x', 2, 17, 18),
                     ('x', 'x', 11, 'x', 'x', 14, 6, 'x', 15, 'x', 'x', 18, 'x', 'x', 'x'),
                     (8, 'x', 5, 1, 7, 14, 'x', 'x', 'x', 'x', 14, 7, 'x', 8, 'x'))
    
    num_rows = 15
    num_cols = 15
    districts = {1: (0, 2), 2: (3, 8), 3: (9, 14)}
    start = (2, 0)
    end = (6, 14)
    
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
                new_cost = g + initial_state[new_row][new_col]
                new_pos = (new_row, new_col)
                
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_pos], new_pos))
    
    return None


def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # Additionally, the heuristic ensures that Ben visits at least one workshop in each district
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    
    for district in districts.values():
        if district[0] <= current[0] <= district[1]:
            h -= 1
    
    return h


print(a_star())
