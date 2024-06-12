
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((-1, -1, 17, 7, -1, -1, 11, 4, 5, 15, 17, 6, 6, 2),
                     (17, -1, -1, 6, -1, -1, -1, -1, 1, 8, -1, -1, -1, 7),
                     (-1, -1, -1, 17, 4, 10, 6, 4, -1, 8, 16, 11, -1, -1),
                     (-1, 4, -1, -1, 10, -1, 8, 10, -1, 11, -1, -1, 1, -1),
                     (-1, -1, 11, 9, 4, -1, 8, 8, -1, -1, -1, 16, 13, 8),
                     (-1, 12, 3, 15, 13, 13, -1, 15, 19, -1, 2, 2, 6, -1),
                     (15, 1, -1, -1, -1, -1, 5, 4, -1, 5, 12, 2, 5, -1),
                     (20, 13, 7, 18, 8, 18, 5, 2, 17, 7, 11, -1, 15, 13),
                     (4, 11, -1, -1, 10, 9, -1, 18, 14, -1, 19, -1, -1, -1),
                     (19, -1, 2, -1, 18, 17, 10, -1, -1, -1, 13, 15, -1, 10),
                     (16, 5, 2, 3, 13, -1, -1, -1, -1, -1, -1, -1, -1, 3),
                     (-1, -1, -1, -1, 17, 9, -1, -1, -1, -1, -1, 6, -1, -1),
                     (11, -1, -1, 9, 14, -1, -1, 16, -1, 15, 13, 13, 15, 1),
                     (9, -1, -1, 10, 14, -1, -1, -1, -1, -1, -1, -1, 1, 19))
    
    num_rows = 14
    num_cols = 14
    districts = {0: (0, 4), 1: (5, 6), 2: (7, 13)}
    start = (4, 12)
    end = (7, 0)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [], start)]
    
    while queue:
        _, g, actions, current = heapq.heappop(queue)
        
        if current == end:
            return actions
        
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current[0] + d[0]
            new_col = current[1] + d[1]
            
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != -1:
                new_state = (new_row, new_col)
                new_cost = g + initial_state[new_row][new_col]
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state))
    
    return None

def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the destination
    # If the current position is in a district, the heuristic is the Manhattan distance to the nearest workshop in the next district
    current_district = None
    for district, bounds in districts.items():
        if bounds[0] <= current[0] <= bounds[1]:
            current_district = district
            break
    
    if current_district is not None:
        next_district = (current_district + 1) % len(districts)
        nearest_workshop = (districts[next_district][0], end[1])
        return abs(nearest_workshop[0] - current[0]) + abs(nearest_workshop[1] - current[1])
    else:
        return abs(end[0] - current[0]) + abs(end[1] - current[1])

print(a_star())
