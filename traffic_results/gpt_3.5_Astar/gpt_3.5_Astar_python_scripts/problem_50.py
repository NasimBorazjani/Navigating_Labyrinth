
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((12, 17, 10, 'x', 'x', 'x', 'x', 9, 15, 5, 'x', 'x'),
                     ('x', 'x', 'x', 'x', 'x', 12, 20, 9, 19, 8, 12, 11),
                     (9, 'x', 'x', 2, 'x', 2, 1, 9, 8, 14, 16, 'x'),
                     (19, 'x', 1, 20, 7, 9, 18, 'x', 18, 7, 'x', 'x'),
                     (5, 2, 11, 9, 'x', 5, 4, 16, 'x', 1, 'x', 10),
                     (10, 8, 8, 4, 11, 11, 'x', 'x', 5, 'x', 'x', 'x'),
                     (15, 15, 'x', 'x', 13, 5, 19, 'x', 'x', 15, 'x', 'x'),
                     (15, 16, 9, 18, 'x', 'x', 16, 'x', 'x', 'x', 5, 12),
                     ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
                     ('x', 'x', 14, 14, 'x', 'x', 15, 6, 6, 'x', 'x', 15),
                     ('x', 'x', 'x', 'x', 'x', 8, 14, 'x', 5, 'x', 'x', 15),
                     ('x', 6, 15, 'x', 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x'))
    
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 6), 3: (7, 11)}
    start = (3, 9)
    end = (7, 1)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end:
            return path
        
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                
                if new_row in range(districts[1][0], districts[1][1] + 1) and len(set([pos for pos in new_path if districts[1][0] <= pos[0] <= districts[1][1]])) < 2:
                    continue
                if new_row in range(districts[2][0], districts[2][1] + 1) and len(set([pos for pos in new_path if districts[2][0] <= pos[0] <= districts[2][1]])) < 2:
                    continue
                if new_row in range(districts[3][0], districts[3][1] + 1) and len(set([pos for pos in new_path if districts[3][0] <= pos[0] <= districts[3][1]])) < 2:
                    continue
                
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[end[0]][end[1]]
                
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[end[0]][end[1]]
                
                if new not in visited_costs or new_cost < visited_costs[new]:
                    visited_costs[new] = new_cost
                    h = heuristic(new, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, new))
    
    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
