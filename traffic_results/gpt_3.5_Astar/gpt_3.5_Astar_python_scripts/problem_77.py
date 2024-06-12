
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 5, 9, 6, 13, 13, 8, 6, 13, 'x', 13, 'x', 'x', 'x'),
                     (3, 10, 16, 'x', 'x', 3, 13, 1, 11, 9, 7, 6, 'x', 18),
                     (9, 11, 3, 'x', 'x', 6, 13, 'x', 14, 'x', 12, 1, 2, 4),
                     ('x', 17, 13, 'x', 14, 4, 6, 8, 'x', 'x', 1, 'x', 6, 2),
                     (7, 'x', 11, 'x', 14, 'x', 11, 7, 'x', 5, 'x', 1, 12, 'x'),
                     ('x', 20, 20, 19, 'x', 18, 2, 19, 1, 6, 12, 'x', 'x', 16),
                     (8, 5, 7, 11, 'x', 1, 'x', 'x', 'x', 11, 4, 'x', 'x', 3),
                     ('x', 11, 'x', 11, 11, 'x', 'x', 18, 'x', 'x', 'x', 7, 6, 'x'),
                     (2, 2, 14, 5, 5, 'x', 'x', 11, 19, 16, 'x', 14, 7, 19),
                     ('x', 5, 'x', 'x', 7, 'x', 10, 'x', 'x', 'x', 3, 15, 'x', 'x'),
                     (19, 'x', 'x', 'x', 'x', 8, 3, 19, 'x', 18, 'x', 'x', 'x', 9),
                     (17, 'x', 19, 'x', 'x', 'x', 5, 3, 'x', 'x', 7, 4, 'x', 'x'),
                     ('x', 'x', 'x', 'x', 'x', 12, 11, 'x', 'x', 'x', 'x', 'x', 6, 6),
                     ('x', 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 7, 'x', 6, 3))
    
    num_rows = 14
    num_cols = 14
    districts = [(0, 1), (2, 5), (6, 13)]
    start = (6, 1)
    end = (3, 13)
    
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
                new_state = [list(row) for row in state]
                new_state[x][y] = 'x'
                new_state[new_x][new_y] = state[x][y]
                new_state = tuple(tuple(row) for row in new_state)
                new_cost = g + int(state[x][y])
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(x, y, int(state[x][y])], (new_x, new_y), new_state))
    
    return None

def heuristic(state, end, districts):
    # The heuristic is the sum of the Manhattan distances from the current position to the destination workshop in the same district
    # If the current position is in the same district as the destination, the heuristic is the Manhattan distance to the destination
    # If the current position is in a different district, the heuristic is the Manhattan distance to the nearest workshop in the destination district
    x, y = end
    district = None
    for i, (start, stop) in enumerate(districts):
        if start <= x <= stop:
            district = i
            break
    
    if district is not None:
        h = abs(x - end[0]) + abs(y - end[1])
    else:
        min_dist = math.inf
        for i, (start, stop) in enumerate(districts):
            dist = min(abs(x - start) + abs(y - stop), abs(x - stop) + abs(y - stop))
            min_dist = min(min_dist, dist)
        h = min_dist
    
    return h

print(a_star())
