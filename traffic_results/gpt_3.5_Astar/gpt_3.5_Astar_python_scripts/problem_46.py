
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((3, 14, 2, 'x', 'x', 'x', 19, 13, 17, 12, 8, 'x'),
                     (1, 2, 13, 1, 4, 19, 'x', 'x', 16, 'x', 'x', 12),
                     (9, 8, 9, 15, 'x', 12, 'x', 'x', 'x', 'x', 'x', 14),
                     (11, 1, 10, 18, 'x', 16, 1, 'x', 12, 'x', 'x', 'x'),
                     (7, 16, 13, 10, 13, 'x', 14, 'x', 'x', 9, 'x', 7),
                     (19, 7, 7, 20, 13, 14, 18, 'x', 'x', 7, 5, 'x'),
                     (4, 'x', 11, 'x', 'x', 2, 7, 1, 5, 'x', 'x', 'x'),
                     ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 1, 'x'),
                     (4, 'x', 'x', 9, 19, 2, 18, 8, 16, 14, 19, 7),
                     ('x', 'x', 'x', 'x', 9, 'x', 17, 17, 1, 2, 2, 15),
                     (18, 'x', 'x', 'x', 'x', 'x', 'x', 11, 10, 'x', 17, 'x'),
                     (9, 'x', 'x', 'x', 10, 3, 'x', 'x', 13, 'x', 2, 'x'))
    
    num_rows = 12
    num_cols = 12
    districts = {1: [(0, 1), (1, 1)], 2: [(2, 0), (7, 11)], 3: [(8, 0), (11, 10)]}
    start = (1, 0)
    end = (8, 10)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(len(set(districts[d]) & set(path)) > 0 for d in districts):
            return path
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(2) and new_col in range(2):
                    new_cost += 1
                elif new_row in range(2, 8) and new_col in range(2, 8):
                    new_cost += 2
                elif new_row in range(8, 12) and new_col in range(8, 12):
                    new_cost += 3
                
                if new not in visited_costs or new_cost < visited_costs[new]:
                    visited_costs[new] = new_cost
                    h = heuristic(new, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, new))
    
    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
