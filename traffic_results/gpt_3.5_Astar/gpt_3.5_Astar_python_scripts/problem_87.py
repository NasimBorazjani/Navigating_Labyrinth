
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    city_map = [['x', 6, 19, 13, 'x', 16, 11, 6, 14, 15, 7, 'x', 'x', 'x'],
                ['x', 6, 16, 15, 'x', 19, 16, 18, 'x', 8, 10, 'x', 'x', 'x'],
                ['x', 5, 10, 14, 2, 'x', 'x', 'x', 11, 'x', 11, 'x', 'x', 'x'],
                [6, 13, 15, 10, 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 2, 'x'],
                ['x', 15, 10, 6, 6, 8, 10, 9, 11, 'x', 'x', 'x', 16, 'x'],
                ['x', 'x', 'x', 8, 15, 12, 10, 19, 1, 18, 19, 4, 'x', 10],
                [1, 17, 'x', 'x', 6, 8, 4, 'x', 15, 8, 10, 6, 4, 'x'],
                ['x', 'x', 'x', 'x', 13, 'x', 5, 'x', 9, 10, 'x', 'x', 'x', 'x'],
                [12, 'x', 11, 'x', 13, 'x', 11, 7, 5, 13, 'x', 'x', 6, 15],
                ['x', 18, 19, 'x', 'x', 'x', 3, 'x', 16, 11, 'x', 15, 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 'x', 2, 15, 'x', 'x', 8, 'x', 'x', 'x'],
                [11, 'x', 6, 13, 12, 'x', 12, 'x', 'x', 9, 'x', 17, 'x', 'x'],
                ['x', 1, 'x', 18, 18, 3, 'x', 11, 13, 1, 13, 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x', 6, 'x', 'x', 8, 'x', 'x', 'x', 4, 11]]
    
    num_rows = 14
    num_cols = 14
    start = (3, 0)
    end = (6, 12)
    districts = [(0, 2), (3, 5), (6, 13)]
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end:
            return path
        
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_row in range(districts[0][0], districts[0][1] + 1) and len(set([pos[0] for pos in new_path])) >= 2:
                    new_cost += 100
                elif new_row in range(districts[1][0], districts[1][1] + 1) and len(set([pos[0] for pos in new_path])) >= 2:
                    new_cost += 100
                elif new_row in range(districts[2][0], districts[2][1] + 1) and len(set([pos[0] for pos in new_path])) >= 2:
                    new_cost += 100
                
                if new not in visited_costs or new_cost < visited_costs[new]:
                    visited_costs[new] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, new_path, new))
    
    return None

print(a_star())
