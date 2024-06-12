
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((13, 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x', 6),
                     ('x', 'x', 'x', 8, 10, 'x', 17, 'x', 15, 14),
                     ('x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11),
                     ('x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'),
                     (18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5),
                     (11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1),
                     ('x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'),
                     ('x', 8, 15, 17, 16, 6, 'x', 3, 'x', 10),
                     (3, 'x', 'x', 'x', 8, 9, 10, 'x', 6, 'x'),
                     (6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x'))
    
    num_rows = 10
    num_cols = 10
    districts = {1: (0, 1), 2: (2, 4), 3: (5, 9)}
    start = (1, 8)
    end = (4, 1)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [], start)]
    
    while queue:
        _, g, actions, current = heapq.heappop(queue)
        
        if current == end:
            return actions
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_district = get_district(new_row, districts)
                if new_row == end[0] and new_col == end[1]:
                    new_district = get_district(end[0], districts)
                if new_district not in [get_district(row, districts) for row in [action[0] for action in actions]]:
                    if (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                        visited_costs[(new_row, new_col)] = new_cost
                        heapq.heappush(queue, (g + heuristic((new_row, new_col), end, districts), new_cost, actions + [(new_row, new_col)], (new_row, new_col)))
    
    return None

def get_district(row, districts):
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None

def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # Additionally, we add a penalty if the current position is not in the same district as the end position
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    current_district = get_district(current[0], districts)
    end_district = get_district(end[0], districts)
    if current_district != end_district:
        h += 10
    return h

print(a_star())
