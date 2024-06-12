
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((math.inf, math.inf, math.inf, 6, 9, math.inf, math.inf, 10, 14, 7, 3, 12),
                     (math.inf, 11, math.inf, 3, 14, 16, 17, 1, 4, 14, 8, 16),
                     (3, math.inf, math.inf, math.inf, 6, 1, 18, 16, math.inf, 6, 3, 11),
                     (math.inf, math.inf, 11, 4, 8, math.inf, math.inf, 1, 3, 9, 8, 7),
                     (math.inf, math.inf, 3, math.inf, math.inf, math.inf, 8, 14, 18, math.inf, math.inf, 18),
                     (4, 1, math.inf, math.inf, math.inf, 14, math.inf, math.inf, math.inf, 3, 4, 20),
                     (1, math.inf, math.inf, math.inf, 14, 19, 15, math.inf, math.inf, 3, 16, 15),
                     (math.inf, math.inf, 6, 18, math.inf, math.inf, 16, 1, math.inf, 3, math.inf, 11),
                     (math.inf, 3, math.inf, 15, math.inf, 19, 10, math.inf, math.inf, math.inf, math.inf, math.inf),
                     (math.inf, 9, math.inf, math.inf, math.inf, math.inf, 17, 17, math.inf, 16, math.inf, 13),
                     (math.inf, math.inf, 8, math.inf, math.inf, 1, math.inf, math.inf, math.inf, 19, 19, 1),
                     (math.inf, 3, 9, math.inf, math.inf, math.inf, 1, math.inf, 10, 11, 8, math.inf))
    
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 1), 2: (2, 5), 3: (6, 11)}
    start = (1, 3)
    end = (6, 10)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(len(set(path[districts[d][0]:districts[d][1]+1])) > 1 for d in districts):
            return path
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != math.inf:
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic((new_row, new_col), end, districts), new_cost, new_path, (new_row, new_col)))
    
    return None

def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # Additionally, we add a penalty if the current position is not in a district that has been visited
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    
    for d in districts:
        if current[0] in range(districts[d][0], districts[d][1]+1):
            break
    else:
        h += 10
    
    return h

print(a_star())
