
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((13, 'x', 10, 17, 'x', 4, 8, 'x', 7, 'x', 12, 19, 4),
                      (17, 'x', 8, 11, 7, 'x', 'x', 19, 'x', 11, 'x', 13, 18),
                      (15, 6, 2, 12, 16, 7, 'x', 14, 'x', 2, 'x', 14, 4),
                      ('x', 18, 4, 'x', 'x', 'x', 13, 14, 2, 4, 20, 10, 7),
                      (7, 2, 19, 16, 'x', 'x', 'x', 18, 'x', 'x', 'x', 2, 2),
                      (10, 17, 14, 7, 17, 3, 3, 19, 'x', 19, 'x', 'x', 9),
                      (9, 'x', 'x', 'x', 5, 18, 13, 6, 'x', 'x', 'x', 19, 10),
                      ('x', 'x', 'x', 'x', 'x', 2, 7, 4, 'x', 'x', 'x', 'x', 'x'),
                      ('x', 'x', 6, 3, 'x', 1, 'x', 'x', 14, 'x', 18, 'x', 1),
                      (14, 'x', 4, 18, 14, 12, 'x', 'x', 'x', 'x', 2, 'x', 13),
                      (12, 'x', 3, 1, 12, 9, 'x', 6, 'x', 'x', 16, 'x', 18),
                      (13, 'x', 11, 5, 3, 4, 'x', 'x', 'x', 'x', 'x', 'x', 18),
                      (15, 9, 9, 1, 'x', 6, 'x', 'x', 14, 'x', 'x', 1, 14))
    num_rows = 13
    num_cols = 13
    districts = {1: [(0, 1), (1, 1)], 2: [(2, 1), (5, 1)], 3: [(6, 1), (12, 1)]}
    start = (5, 1)
    end = (2, 11)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], start)]


    while queue:
        _, g, actions, current = heapq.heappop(queue)


        # If Ben reaches the destination, return the path taken
        if current == end:
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                # Calculate the cost of moving to the new position, which is the travel time
                new_cost = initial_state[new_row][new_col]
                # Ben must visit at least 1 workshop in each district on his path
                for district, workshops in districts.items():
                    if new_position in workshops:
                        # If the new position is in a district, add a small cost to encourage visiting workshops in each district
                        new_cost += 0.1
                # If the new position has not been visited or a lower cost path is found, add it to the queue
                if new_position not in visited_costs or g + new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = g + new_cost
                    h = heuristic(new_position, end)
                    heapq.heappush(queue, (g + h, g + new_cost, actions + [new_position], new_position))
    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the destination
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
