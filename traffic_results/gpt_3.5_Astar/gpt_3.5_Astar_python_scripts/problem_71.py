
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 12, 'x', 'x', 'x', 5, 9, 14, 6, 'x', 3, 14, 'x'),
                     ('x', 'x', 3, 'x', 11, 'x', 13, 'x', 'x', 'x', 'x', 9, 8),
                     ('x', 18, 'x', 'x', 'x', 13, 4, 5, 'x', 'x', 'x', 13, 'x'),
                     (10, 4, 'x', 'x', 'x', 'x', 'x', 18, 'x', 15, 'x', 'x', 'x'),
                     ('x', 1, 7, 'x', 7, 6, 'x', 3, 'x', 2, 'x', 'x', 5),
                     ('x', 15, 5, 'x', 'x', 10, 'x', 19, 'x', 'x', 'x', 10, 6),
                     ('x', 18, 1, 2, 'x', 7, 16, 19, 'x', 'x', 10, 8, 8),
                     (8, 'x', 'x', 6, 2, 'x', 'x', 'x', 7, 11, 5, 11, 2),
                     ('x', 4, 1, 1, 5, 12, 3, 6, 2, 1, 'x', 3, 8),
                     ('x', 'x', 5, 5, 14, 15, 7, 'x', 'x', 11, 'x', 7, 9),
                     ('x', 6, 12, 16, 17, 'x', 'x', 4, 'x', 19, 9, 5, 'x'),
                     (12, 'x', 4, 'x', 8, 4, 'x', 5, 'x', 'x', 'x', 5, 'x'),
                     ('x', 5, 'x', 'x', 'x', 'x', 'x', 7, 'x', 'x', 11, 'x', 'x'))
    
    num_rows = 13
    num_cols = 13
    districts = {1: (0, 4), 2: (5, 5), 3: (6, 12)}
    start = (6, 12)
    end = (4, 1)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(1 in [1 if districts[i][0] <= workshop[0] <= districts[i][1] else 0 for i in range(1, 4)] for workshop in path):
            return path
        
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(districts[1][0], districts[1][1] + 1) and 1 not in [1 if districts[i][0] <= workshop[0] <= districts[i][1] else 0 for i in range(1, 4)]:
                    continue
                
                if new_row in range(districts[2][0], districts[2][1] + 1) and 2 not in [1 if districts[i][0] <= workshop[0] <= districts[i][1] else 0 for i in range(1, 4)]:
                    continue
                
                if new_row in range(districts[3][0], districts[3][1] + 1) and 3 not in [1 if districts[i][0] <= workshop[0] <= districts[i][1] else 0 for i in range(1, 4)]:
                    continue
                
                if new_row in range(districts[1][0], districts[1][1] + 1) and new_col in range(districts[1][0], districts[1][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(districts[2][0], districts[2][1] + 1) and new_col in range(districts[2][0], districts[2][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(districts[3][0], districts[3][1] + 1) and new_col in range(districts[3][0], districts[3][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(districts[1][0], districts[1][1] + 1) and new_col in range(districts[2][0], districts[2][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(districts[1][0], districts[1][1] + 1) and new_col in range(districts[3][0], districts[3][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                
                if new_row in range(districts[2][0], districts[2][1] + 1) and new_col in range(districts[3][0], districts[3][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_path, (new_row, new_col)))
    
    return None

print(a_star())
