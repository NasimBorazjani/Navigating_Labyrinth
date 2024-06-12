
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 2, 'x', 12, 3, 8, 'x', 1, 5, 'x', 'x', 14, 'x', 5, 'x'),
        (5, 'x', 'x', 9, 19, 10, 10, 'x', 'x', 14, 16, 'x', 'x', 17, 'x'),
        (7, 4, 7, 18, 2, 7, 16, 'x', 7, 'x', 9, 'x', 'x', 6, 'x'),
        (9, 'x', 14, 'x', 'x', 14, 7, 9, 18, 11, 14, 8, 13, 14, 15),
        (8, 4, 'x', 17, 'x', 7, 15, 'x', 'x', 19, 'x', 10, 'x', 12, 13),
        (7, 11, 5, 6, 'x', 13, 'x', 'x', 15, 4, 9, 17, 19, 6, 8),
        (13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 4, 10, 'x', 7, 7, 17, 9),
        ('x', 'x', 6, 'x', 'x', 17, 12, 11, 'x', 'x', 'x', 10, 15, 14, 'x'),
        (16, 'x', 5, 19, 'x', 19, 'x', 4, 11, 16, 'x', 'x', 12, 'x', 'x'),
        ('x', 'x', 14, 'x', 'x', 19, 'x', 'x', 4, 13, 7, 'x', 'x', 'x', 8),
        ('x', 4, 'x', 13, 7, 14, 'x', 'x', 2, 15, 9, 11, 'x', 'x', 'x'),
        ('x', 'x', 'x', 'x', 'x', 19, 'x', 6, 2, 'x', 'x', 'x', 4, 7, 'x'),
        (17, 12, 10, 3, 5, 18, 'x', 'x', 'x', 11, 'x', 19, 13, 'x', 'x'),
        (1, 'x', 5, 'x', 17, 'x', 17, 'x', 7, 18, 'x', 'x', 8, 'x', 'x'),
        ('x', 'x', 'x', 'x', 'x', 'x', 2, 9, 'x', 10, 3, 'x', 'x', 15, 2)
    )
    
    num_rows = 15
    num_cols = 15
    districts = [(0, 2), (3, 6), (7, 14)]
    start = (3, 2)
    end = (7, 13)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(len(set(path).intersection(range(start, end+1))) > 0 for start, end in districts):
            return path
        
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, (new_row, new_col)))
    
    return None

print(a_star())
