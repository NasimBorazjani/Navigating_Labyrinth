
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, 'x', 3, 'x'),
                     ('x', 11, 'x', 'x', 'x', 12, 'x', 19, 15, 4, 'x', 'x', 'x', 'x', 'x'),
                     (4, 1, 'x', 8, 'x', 12, 17, 'x', 14, 4, 9, 11, 13, 6, 19),
                     (2, 'x', 6, 14, 15, 'x', 18, 9, 'x', 10, 10, 'x', 'x', 1, 'x'),
                     ('x', 11, 'x', 8, 'x', 5, 'x', 8, 7, 6, 'x', 'x', 13, 6, 'x'),
                     ('x', 'x', 'x', 17, 'x', 13, 'x', 'x', 'x', 'x', 18, 19, 5, 'x', 'x'),
                     ('x', 12, 18, 'x', 'x', 'x', 19, 'x', 12, 'x', 11, 7, 19, 12, 'x'),
                     (6, 6, 'x', 6, 4, 'x', 18, 'x', 'x', 15, 18, 'x', 6, 8, 'x'),
                     (10, 10, 'x', 'x', 6, 4, 11, 19, 'x', 9, 'x', 2, 'x', 3, 14),
                     ('x', 18, 14, 10, 'x', 1, 'x', 6, 'x', 15, 'x', 6, 'x', 14, 'x'),
                     ('x', 'x', 7, 10, 'x', 2, 'x', 7, 14, 4, 11, 'x', 'x', 'x', 'x'),
                     (12, 'x', 6, 'x', 8, 5, 6, 6, 8, 'x', 'x', 'x', 4, 7, 'x'),
                     ('x', 'x', 1, 8, 10, 4, 10, 17, 19, 11, 2, 'x', 'x', 'x', 16),
                     ('x', 'x', 'x', 17, 8, 19, 'x', 14, 'x', 17, 17, 5, 7, 6, 7),
                     (1, 'x', 14, 'x', 3, 'x', 18, 6, 18, 8, 'x', 13, 10, 'x', 'x'))
    
    num_rows = 15
    num_cols = 15
    districts = {1: (0, 4), 2: (5, 8), 3: (9, 14)}
    start = (7, 0)
    end = (4, 13)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], start, initial_state)]
    
    while queue:
        _, g, actions, current_pos, state = heapq.heappop(queue)
        
        if current_pos == end:
            return actions
        
        x, y = current_pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < num_rows and 0 <= new_y < num_cols and state[new_x][new_y] != 'x':
                new_pos = (new_x, new_y)
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                new_state = tuple(tuple(row) for row in new_state)
                new_cost = g + int(state[new_x][new_y])
                
                district_visited = all(any(state[i][j] != 'x' for j in range(num_cols)) for i in range(districts[1][0], districts[1][1] + 1)
                                     ) and all(any(state[i][j] != 'x' for j in range(num_cols)) for i in range(districts[2][0], districts[2][1] + 1)
                                     ) and all(any(state[i][j] != 'x' for j in range(num_cols)) for i in range(districts[3][0], districts[3][1] + 1))
                
                if district_visited and (new_state not in visited_costs or new_cost < visited_costs[new_state]):
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_pos, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_pos], new_pos, new_state))
    
    return None


def heuristic(current_pos, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current_pos[0] - end[0]) + abs(current_pos[1] - end[1])


print(a_star())
