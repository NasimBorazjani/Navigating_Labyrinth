
import heapq
import math

def a_star():
    # Define the city map as a 2D list
    city_map = [
        ['x', 9, 4, 8, 'x', 'x', 4, 'x', 8, 12, 'x', 'x', 14],
        [17, 'x', 3, 'x', 6, 'x', 12, 2, 'x', 'x', 'x', 5, 19],
        ['x', 8, 8, 'x', 5, 'x', 15, 14, 14, 3, 10, 12, 3],
        [4, 'x', 16, 'x', 'x', 11, 12, 'x', 'x', 6, 5, 18, 19],
        ['x', 4, 9, 17, 'x', 'x', 'x', 13, 4, 7, 'x', 2, 16],
        [3, 6, 'x', 'x', 'x', 10, 5, 'x', 18, 10, 9, 20, 4],
        ['x', 'x', 'x', 14, 18, 'x', 'x', 'x', 'x', 16, 'x', 'x', 4],
        [14, 12, 'x', 4, 12, 11, 19, 'x', 3, 2, 'x', 13, 'x'],
        [19, 6, 2, 18, 'x', 'x', 8, 7, 1, 12, 19, 'x', 'x'],
        ['x', 9, 16, 17, 5, 12, 19, 8, 'x', 3, 10, 'x', 'x'],
        ['x', 10, 3, 'x', 14, 16, 2, 16, 4, 10, 18, 15, 'x'],
        [15, 5, 5, 'x', 13, 'x', 3, 7, 'x', 4, 1, 17, 15],
        [5, 2, 6, 'x', 'x', 'x', 'x', 8, 16, 'x', 'x', 'x', 'x']
    ]
    
    num_rows = 13
    num_cols = 13
    districts = {1: (0, 2), 2: (3, 7), 3: (8, 12)}
    start = (7, 1)
    end = (2, 10)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(len(set(path[districts[d][0]:districts[d][1]+1])) > 1 for d in districts):
            return path
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_row == end[0] and new_col == end[1]:
                    new_cost += city_map[end[0]][end[1]]
                
                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    h = heuristic(new_row, new_col, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))
    
    return None

def heuristic(current, end):
    # Calculate the Manhattan distance heuristic
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
