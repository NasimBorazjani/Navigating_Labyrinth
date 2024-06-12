
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 'x', 6, 'x', 7, 'x', 9, 4, 11),
                     ('x', 3, 'x', 6, 5, 3, 15, 'x', 3),
                     ('x', 'x', 'x', 4, 'x', 9, 1, 8, 'x'),
                     (15, 18, 1, 6, 5, 10, 6, 14, 8),
                     (18, 10, 7, 18, 2, 'x', 'x', 'x', 7),
                     (11, 9, 16, 'x', 11, 'x', 11, 'x', 17),
                     (7, 'x', 18, 'x', 8, 10, 20, 6, 'x'),
                     (15, 4, 17, 'x', 16, 2, 12, 16, 'x'),
                     (9, 10, 18, 17, 9, 6, 7, 'x', 15))
    num_rows = 9
    num_cols = 9
    districts = {1: [(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (2, 6), (2, 8)],
                 2: [(4, 0), (4, 1), (4, 2), (4, 3), (5, 0), (5, 1), (5, 3), (5, 6), (5, 8), (6, 1), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)],
                 3: [(7, 0), (7, 1), (7, 2), (7, 4), (7, 5), (7, 6), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7), (8, 8)]}
    start = (3, 0)
    end = (6, 6)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], [start])]


    while queue:
        _, g, actions, path = heapq.heappop(queue)
        current_position = path[-1]


        # If Ben reaches the destination workshop, return the path taken
        if current_position == end:
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_position[0] + d_row, current_position[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_path = path + [new_position]
                # Check if Ben has visited at least 1 workshop in each district on the new path
                if all(any(pos in district for pos in new_path) for district in districts.values()):
                    # Calculate the cost of moving to the new position
                    new_cost = g + int(initial_state[new_row][new_col])
                    # If the new position has not been visited or a lower cost path is found, add it to the queue
                    if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                        visited_costs[new_position] = new_cost
                        h = heuristic(new_position, end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_path))
    return None


def heuristic(current_position, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the destination
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(current_position[0] - end[0]) + abs(current_position[1] - end[1])


print(a_star())
