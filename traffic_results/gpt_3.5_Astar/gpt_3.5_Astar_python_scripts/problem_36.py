
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 11, 5, 18, 'x', 14, 7, 'x', 15, 11, 14),
                     ('x', 'x', 'x', 'x', 13, 13, 11, 17, 8, 13, 'x'),
                     ('x', 8, 1, 5, 17, 'x', 4, 8, 20, 7, 4),
                     ('x', 10, 'x', 'x', 18, 1, 'x', 'x', 20, 'x', 'x'),
                     (18, 15, 'x', 6, 'x', 4, 3, 4, 3, 13, 'x'),
                     (5, 1, 'x', 4, 'x', 'x', 'x', 11, 'x', 14, 18),
                     (19, 19, 'x', 'x', 'x', 'x', 15, 'x', 10, 'x', 'x'),
                     (15, 5, 7, 'x', 14, 6, 'x', 'x', 'x', 13, 'x'),
                     (18, 7, 'x', 19, 'x', 12, 'x', 'x', 15, 'x', 'x'),
                     (10, 9, 'x', 1, 'x', 'x', 15, 'x', 11, 'x', 2),
                     ('x', 'x', 8, 'x', 19, 'x', 1, 3, 'x', 'x', 8))
    
    num_rows = 11
    num_cols = 11
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (6, 0)], 3: [(7, 0), (10, 0)]}
    destination = (3, 8)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if Ben has reached the destination workshop
        if (3, 8) not in actions and state[3][8] != 'x':
            continue
        
        # Check if Ben has visited at least one workshop in each district
        visited_districts = set()
        for action in actions:
            for district, workshops in districts.items():
                if action in workshops:
                    visited_districts.add(district)
        if len(visited_districts) < 3:
            continue
        
        # Check if Ben has reached the destination workshop
        if actions and actions[-1] == (3, 8):
            return actions
        
        # Generate all possible actions from the current state, which includes moving to neighboring workshops
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = actions[-1][0] + d_row
            new_col = actions[-1][1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
                new_state = [list(row) for row in state]
                new_state[new_row][new_col] = 'x'
                new_state = tuple(tuple(row) for row in new_state)
                new_cost = g + int(state[new_row][new_col])
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_row, new_col, destination)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], new_state))
    
    return None

def heuristic(row, col, destination):
    # Calculate the Manhattan distance from the current position to the destination
    return abs(row - destination[0]) + abs(col - destination[1])

print(a_star())
