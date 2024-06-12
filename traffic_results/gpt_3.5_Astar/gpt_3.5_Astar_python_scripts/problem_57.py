
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((17, 9, 11, 5, 19, 4, 18, 'x', 5, 8, 'x', 'x'),
                     (6, 13, 'x', 9, 2, 20, 11, 20, 7, 'x', 'x', 3),
                     (4, 17, 'x', 18, 2, 10, 'x', 16, 'x', 18, 'x', 'x'),
                     (12, 10, 9, 14, 'x', 'x', 12, 6, 1, 2, 'x', 'x'),
                     (5, 'x', 'x', 3, 'x', 4, 9, 14, 8, 'x', 10, 12),
                     (1, 'x', 6, 3, 18, 18, 17, 17, 10, 'x', 'x', 10),
                     (13, 'x', 'x', 'x', 'x', 'x', 14, 'x', 1, 19, 'x', 7),
                     (11, 'x', 'x', 5, 9, 'x', 18, 19, 13, 13, 'x', 10),
                     ('x', 'x', 11, 'x', 17, 'x', 'x', 'x', 14, 17, 'x', 13),
                     (19, 'x', 'x', 'x', 'x', 19, 12, 7, 3, 14, 'x', 9),
                     ('x', 12, 7, 15, 1, 'x', 16, 11, 9, 17, 'x', 'x'),
                     ('x', 'x', 'x', 10, 'x', 1, 7, 'x', 'x', 'x', 6, 12))
    
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 6), 3: (7, 11)}
    start = (7, 0)
    end = (3, 8)
    
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
                if new_cost <= 166 and new_district not in [get_district(x, districts) for x in actions]:
                    new_pos = (new_row, new_col)
                    if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                        visited_costs[new_pos] = new_cost
                        h = heuristic(new_pos, end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_pos], new_pos))
    
    return None

def get_district(row, districts):
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None

def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
