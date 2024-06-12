
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((11, 'x', 'x', 'x', 15, 5, 18, 4, 1, 17, 14, 'x', 9),
                     ('x', 10, 10, 7, 12, 12, 6, 'x', 'x', 8, 4, 19, 11),
                     (17, 'x', 'x', 12, 8, 'x', 'x', 'x', 14, 19, 'x', 18, 16),
                     (17, 'x', 16, 'x', 'x', 17, 4, 'x', 15, 'x', 'x', 'x', 17),
                     (17, 'x', 'x', 6, 'x', 'x', 12, 6, 10, 3, 11, 'x', 19),
                     (10, 'x', 9, 15, 17, 4, 'x', 'x', 'x', 'x', 14, 17, 18),
                     (4, 'x', 'x', 'x', 'x', 13, 18, 13, 'x', 17, 12, 'x', 19),
                     ('x', 2, 11, 7, 6, 14, 9, 'x', 12, 17, 9, 13, 14),
                     ('x', 18, 16, 'x', 'x', 'x', 11, 6, 12, 'x', 'x', 10, 'x'),
                     (5, 3, 'x', 'x', 'x', 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'),
                     (18, 'x', 'x', 'x', 'x', 14, 'x', 'x', 13, 1, 3, 'x', 'x'),
                     (1, 16, 10, 'x', 'x', 14, 13, 'x', 10, 'x', 1, 'x', 18),
                     (8, 'x', 'x', 10, 2, 10, 'x', 'x', 'x', 'x', 'x', 13, 5))
    
    num_rows = 13
    num_cols = 13
    districts = {1: (0, 2), 2: (3, 7), 3: (8, 12)}
    start = (8, 11)
    end = (2, 3)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], [start], initial_state)]
    
    while queue:
        _, g, actions, path, state = heapq.heappop(queue)
        
        current_position = path[-1]
        
        if current_position == end:
            return actions
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current_position[0] + d_row, current_position[1] + d_col
            
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x' and (new_row, new_col) not in path:
                new_path = path + [(new_row, new_col)]
                new_state = [list(row) for row in state]
                new_state[new_row][new_col] = 'x'
                new_state = tuple(tuple(row) for row in new_state)
                
                new_cost = g + state[new_row][new_col]
                
                if all(districts[dist][0] in [pos[0] for pos in new_path] for dist in districts) and all(districts[dist][1] in [pos[0] for pos in new_path] for dist in districts):
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_path, end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_path[-1]], new_path, new_state))
    
    return None

def heuristic(path, end):
    # The heuristic is the Manhattan distance from the current position to the end position
    return abs(path[-1][0] - end[0]) + abs(path[-1][1] - end[1])

print(a_star())
