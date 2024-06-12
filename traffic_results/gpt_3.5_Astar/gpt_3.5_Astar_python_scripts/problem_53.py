
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((18, 'x', 'x', 14, 5, 'x', 'x', 5, 18, 'x', 3, 'x'),
                     ('x', 'x', 'x', 9, 2, 2, 'x', 15, 14, 12, 'x', 18),
                     ('x', 'x', 3, 16, 3, 9, 'x', 16, 'x', 14, 'x', 17),
                     ('x', 'x', 'x', 19, 7, 20, 'x', 'x', 11, 4, 'x', 4),
                     (7, 'x', 8, 11, 'x', 1, 15, 5, 'x', 'x', 11, 'x'),
                     ('x', 'x', 'x', 'x', 'x', 'x', 6, 11, 'x', 'x', 'x', 8),
                     ('x', 15, 2, 'x', 'x', 18, 'x', 1, 16, 15, 6, 5),
                     ('x', 4, 18, 8, 9, 'x', 'x', 17, 20, 13, 'x', 10),
                     ('x', 16, 'x', 'x', 19, 'x', 17, 'x', 13, 11, 14, 2),
                     (12, 'x', 11, 'x', 3, 'x', 5, 3, 'x', 13, 17, 6),
                     (14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 16),
                     (12, 'x', 'x', 'x', 12, 'x', 10, 'x', 18, 14, 8, 'x'))
    
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 6), 3: (7, 11)}
    start = (3, 3)
    end = (7, 11)
    
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
                if new_district not in [get_district(row, districts) for row in actions] or new_row == end[0] and new_col == end[1]:
                    if (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                        visited_costs[(new_row, new_col)] = new_cost
                        h = heuristic((new_row, new_col), end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], (new_row, new_col)))
    
    return None

def get_district(row, districts):
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None

def heuristic(current, end):
    # Calculate the Manhattan distance as the heuristic
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
