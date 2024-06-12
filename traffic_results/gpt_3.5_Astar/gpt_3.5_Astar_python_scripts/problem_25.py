
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 'x', 6, 'x', 'x', 'x', 'x', 15, 'x', 'x'),
                     ('x', 17, 13, 13, 'x', 12, 'x', 3, 10, 2),
                     ('x', 5, 13, 15, 4, 'x', 'x', 20, 6, 2),
                     ('x', 9, 'x', 6, 2, 16, 18, 9, 13, 'x'),
                     ('x', 'x', 15, 17, 'x', 10, 11, 'x', 'x', 'x'),
                     (3, 'x', 3, 17, 8, 'x', 1, 'x', 16, 'x'),
                     ('x', 'x', 13, 15, 'x', 'x', 11, 'x', 'x', 4),
                     ('x', 'x', 12, 1, 'x', 'x', 'x', 14, 11, 'x'),
                     ('x', 14, 'x', 'x', 19, 13, 4, 'x', 'x', 'x'),
                     (1, 'x', 'x', 14, 11, 19, 2, 17, 2, 5))
    num_rows = 10
    num_cols = 10
    districts = {1: [(0, 2), (1, 1), (1, 2), (1, 3), (1, 5), (1, 7), (1, 8), (1, 9), (2, 1), (2, 2), (2, 3), (2, 4), (2, 7), (2, 8), (2, 9)],
                 2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 2), (4, 5), (4, 6)],
                 3: [(5, 1), (5, 3), (5, 6), (6, 2), (6, 6), (7, 2), (7, 7), (8, 1), (8, 4), (8, 5), (8, 7), (9, 0), (9, 3), (9, 5), (9, 7), (9, 8)]}
    start = (2, 9)
    end = (5, 2)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], [start])]


    while queue:
        _, g, actions, path = heapq.heappop(queue)
        current_position = path[-1]


        # If Ben has reached the destination workshop and visited at least 1 workshop in each district, return the path
        if current_position == end and all(any(workshop in district for workshop in path) for district in districts.values()):
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_position[0] + d_row, current_position[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_path = path + [new_position]
                # The cost so far is the sum of travel times from the current position to the new position
                new_cost = g + int(initial_state[new_row][new_col])
              
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_path))
    return None


def heuristic(current_position, end):
    # The heuristic is the Manhattan distance between the current position and the destination
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the heuristic estimate, if the position is moved toward the destination, otherwise the estimated cost of the successor node is the same or higher
    return abs(current_position[0] - end[0]) + abs(current_position[1] - end[1])


print(a_star())
