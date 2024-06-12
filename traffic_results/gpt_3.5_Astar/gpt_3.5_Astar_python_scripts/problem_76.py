
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 12, 8, 4, 4, 16, 8, 'x', 'x', 17, 18, 9, 'x', 16),
                     (2, 9, 'x', 1, 4, 13, 20, 11, 2, 'x', 11, 7, 14, 12),
                     ('x', 'x', 'x', 'x', 17, 15, 8, 12, 'x', 'x', 7, 'x', 'x', 'x'),
                     (2, 2, 'x', 5, 14, 'x', 1, 5, 4, 14, 7, 'x', 'x', 'x'),
                     (19, 'x', 11, 1, 19, 19, 12, 'x', 12, 13, 5, 3, 17, 17),
                     ('x', 'x', 'x', 'x', 'x', 1, 'x', 'x', 4, 'x', 'x', 'x', 8, 19),
                     (6, 'x', 10, 'x', 7, 1, 11, 'x', 'x', 3, 'x', 3, 2, 'x'),
                     (19, 'x', 3, 11, 'x', 6, 11, 'x', 12, 14, 10, 'x', 11, 18),
                     (13, 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 'x', 'x', 10, 5),
                     (19, 'x', 'x', 16, 'x', 'x', 18, 'x', 8, 'x', 2, 11, 'x', 12),
                     ('x', 14, 'x', 6, 'x', 18, 'x', 11, 'x', 'x', 14, 11, 2, 'x'),
                     ('x', 'x', 6, 8, 10, 8, 14, 'x', 'x', 13, 'x', 10, 'x', 19),
                     ('x', 19, 'x', 7, 12, 17, 'x', 15, 'x', 16, 19, 'x', 5, 'x'),
                     (8, 'x', 17, 'x', 'x', 5, 15, 'x', 'x', 16, 1, 'x', 'x', 17))
    
    num_rows = 14
    num_cols = 14
    districts = [(0, 2), (3, 7), (8, 13)]
    start = (4, 3)
    end = (8, 13)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state[end[0]][end[1]] != 'x':
            return actions
        
        # Generate all possible actions from the current state, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = state[start[0]][start[1]] + d_row, state[start[0]][start[1]] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
                new_state = [list(row[:]) for row in state]
                new_state[start[0]][start[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[start[0]][start[1]]
                new_state = tuple(tuple(row) for row in new_state)
                new_cost = g + int(state[new_row][new_col])
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], new_state))
    
    return None


def heuristic(state, end, districts):
    # The heuristic function calculates the Manhattan distance from the current position to the destination workshop in the same district
    # If the current position is in the same district as the destination, the heuristic is the Manhattan distance to the destination
    # If the current position is in a different district, the heuristic is the Manhattan distance to the nearest workshop in the destination district
    h = 0
    current_district = None
    for i, (start, end) in enumerate(districts):
        if start <= state[end[0]][end[1]] <= end:
            current_district = i
            break
    
    if current_district is not None:
        h = abs(state[end[0]][end[1]] - end[0]) + abs(state[end[0]][end[1]] - end[1])
    else:
        min_distance = math.inf
        for i, (start, end) in enumerate(districts):
            distance = abs(state[end[0]][end[1]] - end[0]) + abs(state[end[0]][end[1]] - end[1])
            if distance < min_distance:
                min_distance = distance
        h = min_distance
    
    return h


print(a_star())
