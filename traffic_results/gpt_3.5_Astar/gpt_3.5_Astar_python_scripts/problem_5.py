
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[8, 'x', 4, 7, 10, 'x', 12, 5, 'x'],
                ['x', 'x', 4, 11, 16, 4, 12, 15, 'x'],
                [3, 'x', 16, 16, 4, 'x', 'x', 'x', 'x'],
                [11, 6, 3, 12, 8, 2, 19, 14, 'x'],
                [20, 18, 19, 'x', 4, 18, 'x', 15, 13],
                [8, 15, 'x', 16, 11, 'x', 10, 14, 1],
                ['x', 'x', 'x', 19, 'x', 'x', 'x', 'x', 'x'],
                [7, 'x', 'x', 'x', 'x', 'x', 1, 7, 8],
                [15, 3, 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    
    num_rows = 9
    num_cols = 9
    start = (5, 0)
    end = (3, 7)
    districts = [(0, 3), (4, 4), (5, 8)]
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(any(city_map[i][j] != 'x' for j in range(num_cols)) for i in range(num_rows)):
            return path
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if all(new_row not in range(start[0], end[0] + 1) or new_col not in range(district[0], district[1] + 1) for district in districts):
                    continue
                
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    h = heuristic((new_row, new_col), end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))
    
    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
