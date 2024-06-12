
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((19, 12, 'x', 'x', 2, 5, 4, 13, 17, 19, 'x', 2),
                     ('x', 18, 'x', 5, 5, 'x', 'x', 8, 12, 18, 'x', 15),
                     ('x', 9, 4, 10, 7, 20, 'x', 16, 20, 13, 15, 'x'),
                     (8, 'x', 'x', 11, 1, 19, 'x', 14, 6, 'x', 3, 'x'),
                     (10, 'x', 4, 8, 17, 'x', 18, 'x', 7, 'x', 6, 5),
                     ('x', 'x', 3, 1, 8, 18, 'x', 4, 17, 'x', 'x', 13),
                     ('x', 'x', 6, 'x', 'x', 'x', 14, 'x', 'x', 10, 10, 'x'),
                     ('x', 'x', 15, 'x', 'x', 'x', 'x', 'x', 2, 'x', 'x', 'x'),
                     ('x', 'x', 5, 11, 6, 1, 'x', 6, 14, 'x', 'x', 'x'),
                     ('x', 1, 17, 10, 15, 'x', 14, 6, 'x', 'x', 'x', 'x'),
                     (12, 2, 'x', 10, 'x', 'x', 7, 'x', 'x', 'x', 'x', 'x'),
                     ('x', 9, 14, 'x', 9, 18, 14, 'x', 'x', 'x', 6, 'x'))
    num_rows = 12
    num_cols = 12
    districts = {1: [(0, 1), (0, 2)], 2: [(2, 5), (5, 10)], 3: [(6, 11)]}
    start = (6, 2)
    end = (2, 10)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], [start])]


    while queue:
        _, g, actions, path = heapq.heappop(queue)
        current_position = path[-1]


        # If Ben reaches the destination workshop and has visited at least 1 workshop in each district, return the path
        if current_position == end and all(any(pos in district for pos in path) for district in districts.values()):
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_position[0] + d_row, current_position[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_path = path + [new_position]
                # Calculate the cost of moving to the new position
                new_cost = g + initial_state[new_row][new_col]
              
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_path))
    return None


def heuristic(current_position, end):
    # The heuristic is the Manhattan distance between the current position and the destination position
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(current_position[0] - end[0]) + abs(current_position[1] - end[1])


print(a_star())
