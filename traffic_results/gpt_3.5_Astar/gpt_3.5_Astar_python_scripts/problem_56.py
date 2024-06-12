
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((2, math.inf, math.inf, 14, math.inf, 19, 6, math.inf, math.inf, 14, 18, math.inf),
                     (math.inf, 10, 1, 15, math.inf, math.inf, math.inf, math.inf, 17, 2, 9, 12),
                     (13, 14, math.inf, 2, math.inf, math.inf, 10, 10, math.inf, math.inf, math.inf, math.inf),
                     (9, 17, 3, 15, 4, 4, math.inf, 9, 15, 16, math.inf, 9),
                     (10, 7, 3, 8, math.inf, 7, math.inf, 16, 3, 7, math.inf, math.inf),
                     (16, 20, 16, 19, 18, 3, math.inf, math.inf, 11, 14, 5, math.inf),
                     (14, 13, 8, 14, 12, 19, 6, 3, 19, 10, 11, math.inf),
                     (math.inf, 18, math.inf, math.inf, 4, 19, 6, 14, 15, 17, 7, math.inf),
                     (math.inf, 2, math.inf, math.inf, math.inf, math.inf, math.inf, 7, math.inf, 19, math.inf, math.inf),
                     (math.inf, 3, 14, 1, math.inf, 18, 4, 12, math.inf, 3, 10, math.inf),
                     (2, math.inf, 16, 13, math.inf, 17, math.inf, math.inf, 17, 16, 4, 10),
                     (math.inf, 4, 10, math.inf, math.inf, math.inf, 7, math.inf, 19, 7, math.inf, math.inf))
    
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 6), 3: (7, 11)}
    start = (6, 9)
    end = (3, 0)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], start, initial_state)]
    
    while queue:
        _, g, actions, current, state = heapq.heappop(queue)
        
        if current == end:
            return actions
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != math.inf:
                new_state = [list(row) for row in state]
                new_state[current[0]][current[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[current[0]][current[1]]
                new_state = tuple(tuple(row) for row in new_state)
                new_cost = g + new_state[new_row][new_col]
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    district = get_district(new_row, districts)
                    heapq.heappush(queue, (g + new_cost, new_cost, actions + [(new_row, new_col)], (new_row, new_col), new_state))
    
    return None

def get_district(row, districts):
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None

print(a_star())
