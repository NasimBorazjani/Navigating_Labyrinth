
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 'x', 7, 18, 11, 4, 9, 'x', 15, 'x', 'x', 'x', 1, 'x', 'x'),
        ('x', 'x', 14, 'x', 10, 'x', 'x', 'x', 8, 'x', 'x', 16, 1, 'x', 'x'),
        (17, 17, 'x', 'x', 'x', 'x', 'x', 7, 6, 12, 'x', 'x', 'x', 7, 'x'),
        ('x', 'x', 'x', 'x', 10, 'x', 'x', 18, 1, 11, 4, 'x', 13, 10, 16),
        ('x', 'x', 'x', 12, 1, 'x', 'x', 'x', 2, 7, 1, 'x', 2, 'x', 5),
        ('x', 'x', 8, 'x', 12, 'x', 'x', 5, 17, 'x', 2, 'x', 4, 10, 18),
        ('x', 'x', 4, 19, 1, 'x', 18, 7, 'x', 10, 3, 'x', 19, 16, 19),
        (6, 12, 15, 16, 5, 9, 16, 18, 10, 15, 5, 'x', 5, 14, 'x'),
        ('x', 16, 8, 17, 12, 11, 16, 8, 9, 9, 7, 4, 5, 20, 3),
        (19, 17, 15, 'x', 'x', 17, 'x', 3, 2, 2, 11, 7, 8, 16, 1),
        (13, 4, 17, 'x', 'x', 'x', 'x', 5, 'x', 18, 16, 15, 19, 4, 'x'),
        (11, 'x', 'x', 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x'),
        (18, 'x', 'x', 'x', 9, 19, 'x', 16, 6, 'x', 9, 3, 16, 15, 'x'),
        ('x', 'x', 'x', 10, 'x', 'x', 4, 3, 'x', 3, 'x', 16, 18, 'x', 12),
        ('x', 13, 'x', 'x', 'x', 'x', 'x', 10, 5, 'x', 17, 'x', 'x', 7, 'x')
    )
    
    num_rows = 15
    num_cols = 15
    districts = [(0, 4), (5, 8), (9, 14)]
    start = (7, 2)
    end = (4, 14)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = [(0, 0, [start], start)]
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(any(cell != 'x' for cell in row) for row in initial_state):
            return path
        
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + int(initial_state[new_row][new_col])
                new_path = path + [(new_row, new_col)]
                
                if new_row in range(districts[0][0], districts[0][1] + 1) and len(set(row for row, _ in new_path if row in range(districts[0][0], districts[0][1] + 1))) < 2:
                    continue
                if new_row in range(districts[1][0], districts[1][1] + 1) and len(set(row for row, _ in new_path if row in range(districts[1][0], districts[1][1] + 1))) < 2:
                    continue
                if new_row in range(districts[2][0], districts[2][1] + 1) and len(set(row for row, _ in new_path if row in range(districts[2][0], districts[2][1] + 1))) < 2:
                    continue
                
                if new_col in range(districts[0][0], districts[0][1] + 1) and len(set(col for _, col in new_path if col in range(districts[0][0], districts[0][1] + 1))) < 2:
                    continue
                if new_col in range(districts[1][0], districts[1][1] + 1) and len(set(col for _, col in new_path if col in range(districts[1][0], districts[1][1] + 1))) < 2:
                    continue
                if new_col in range(districts[2][0], districts[2][1] + 1) and len(set(col for _, col in new_path if col in range(districts[2][0], districts[2][1] + 1))) < 2:
                    continue
                
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost + abs(new_row - end[0]) + abs(new_col - end[1]), new_cost, new_path, (new_row, new_col))
    
    return None

print(a_star())
