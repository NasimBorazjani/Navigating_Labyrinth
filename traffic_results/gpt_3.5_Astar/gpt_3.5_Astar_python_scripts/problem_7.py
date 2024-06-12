
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 7, 7, 12, 7, 'x', 13, 1, 18),
                     (9, 18, 'x', 4, 19, 8, 'x', 15, 10),
                     (9, 'x', 10, 5, 5, 9, 8, 'x', 'x'),
                     (14, 4, 19, 9, 14, 'x', 'x', 7, 9),
                     (9, 4, 11, 15, 7, 'x', 17, 3, 'x'),
                     (11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'),
                     ('x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'),
                     (3, 'x', 2, 'x', 12, 'x', 'x', 'x', 4),
                     ('x', 'x', 7, 'x', 19, 'x', 'x', 'x', 9))
    num_rows = 9
    num_cols = 9
    districts = {1: [(0, 2), (0, 6), (1, 4), (2, 1)],
                 2: [(3, 0), (3, 5), (4, 2), (5, 2)],
                 3: [(6, 1), (6, 5), (7, 3), (8, 4)]}
    start = (6, 1)
    end = (2, 6)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], start)]


    while queue:
        _, g, actions, current = heapq.heappop(queue)


        # If Ben reaches the destination workshop, return the path taken
        if current == end:
            return actions


        # Generate all possible actions from the current workshop, which includes moving north, south, east, or west
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            # Check if the new position is within the bounds of the city map
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Check if the new position is not a closed workshop
                if initial_state[new_row][new_col] != 'x':
                    new_position = (new_row, new_col)
                    # Calculate the cost of moving to the new position
                    new_cost = g + initial_state[new_row][new_col]
                    # Check if Ben has visited at least one workshop in each district on the path
                    for district, workshops in districts.items():
                        if new_position in workshops and new_position not in actions:
                            # If the new position is in a district that Ben has not visited yet, add it to the actions
                            new_actions = actions + [new_position]
                            # If the new position is not visited yet or a better path is found, add it to the queue
                            if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                                visited_costs[new_position] = new_cost
                                h = heuristic(new_position, end)
                                heapq.heappush(queue, (g + h, new_cost, new_actions, new_position))
    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the destination
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
