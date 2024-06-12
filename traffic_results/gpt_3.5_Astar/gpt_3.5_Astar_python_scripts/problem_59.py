
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'),
                     (5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13),
                     (15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17),
                     ('x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7),
                     (5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14),
                     (16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15),
                     ('x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1),
                     (6, 8, 'x', 3, 'x', 5, 5, 'x', 3, 8, 9, 14),
                     (10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'),
                     (12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16),
                     (4, 'x', 'x', 'x', 11, 'x', 'x', 'x', 18, 16, 'x', 10),
                     ('x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9))
    
    num_rows = 12
    num_cols = 12
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (6, 0)], 3: [(7, 0), (11, 0)]}
    start = (2, 0)
    end = (7, 8)
    
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
                elif new_row in range(2, 7) and new_col in range(2, 7):
                    new_cost += 1
                elif new_row in range(7, 12) and new_col in range(7, 12):
                    new_cost += 1
                
                if new not in visited_costs or new_cost < visited_costs[new]:
                    visited_costs[new] = new_cost
                    h = heuristic(new, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, new))
    
    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
