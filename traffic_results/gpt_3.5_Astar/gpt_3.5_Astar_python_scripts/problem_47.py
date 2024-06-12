
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((5, 'x', 'x', 4, 'x', 12, 7, 11, 8, 3, 19, 'x'),
                     ('x', 'x', 6, 15, 16, 'x', 'x', 4, 'x', 7, 8, 19),
                     (18, 'x', 'x', 15, 'x', 'x', 'x', 8, 4, 16, 7, 9),
                     ('x', 19, 'x', 'x', 'x', 16, 'x', 'x', 17, 15, 'x', 9),
                     (15, 8, 19, 'x', 4, 4, 'x', 'x', 'x', 3, 3, 10),
                     (18, 6, 14, 5, 'x', 18, 19, 15, 18, 19, 12, 5),
                     (12, 'x', 2, 2, 6, 3, 3, 8, 3, 1, 'x', 15),
                     (10, 4, 'x', 9, 15, 3, 'x', 7, 'x', 17, 'x', 'x'),
                     (5, 18, 'x', 17, 'x', 17, 'x', 'x', 15, 'x', 18, 'x'),
                     (4, 'x', 16, 11, 10, 3, 12, 'x', 11, 14, 3, 'x'),
                     ('x', 9, 9, 14, 19, 15, 'x', 1, 10, 19, 6, 'x'),
                     ('x', 'x', 17, 4, 'x', 2, 'x', 7, 'x', 4, 4, 18))
    num_rows = 12
    num_cols = 12
    districts = {1: set(range(5)), 2: set(range(5, 6)), 3: set(range(6, 12))}
    start = (4, 11)
    end = (6, 0)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], start)]


    while queue:
        _, g, actions, current = heapq.heappop(queue)


        # If the current position is the destination, return the actions taken
        if current == end:
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                # Check if Ben has visited at least one workshop in each district on the path to the destination
                if all(len(districts[district].intersection(set([new_position]))) > 0 for district in districts):
                    # Calculate the cost of moving to the new position, which is the travel time
                    new_cost = g + initial_state[new_row][new_col]
                    if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                        visited_costs[new_position] = new_cost
                        # Calculate the heuristic cost, which is the Manhattan distance to the destination
                        h = abs(new_row - end[0]) + abs(new_col - end[1])
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))
    return None


print(a_star())
