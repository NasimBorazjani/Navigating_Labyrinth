
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((6, 16, 'x', 'x', 15, 'x', 14, 11, 'x'),
                     (5, 2, 1, 'x', 3, 'x', 4, 13, 'x'),
                     ('x', 7, 'x', 'x', 13, 'x', 10, 14, 5),
                     (6, 16, 'x', 13, 6, 'x', 16, 'x', 'x'),
                     ('x', 1, 17, 'x', 6, 3, 'x', 'x', 3),
                     (11, 10, 7, 19, 15, 8, 12, 6, 'x'),
                     (18, 'x', 'x', 9, 8, 9, 'x', 'x', 13),
                     (4, 'x', 'x', 'x', 18, 20, 'x', 'x', 'x'),
                     ('x', 'x', 8, 'x', 18, 2, 6, 13, 'x'))
    num_rows = 9
    num_cols = 9
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], 3: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]}
    start = (5, 5)
    end = (1, 0)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], start)]


    while queue:
        _, g, actions, current = heapq.heappop(queue)


        # If Ben reaches the destination, return the actions taken
        if current == end:
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                # Calculate the cost of moving to the new position
                new_cost = g + initial_state[new_row][new_col]
                # Check if Ben has visited at least one workshop in each district on the path
                for district, workshops in districts.items():
                    if new_position in workshops and all(workshop in actions for workshop in workshops):
                        # If the new position is in a district that Ben has not visited yet, add it to the actions
                        if district not in [workshop[0] for workshop in actions]:
                            new_actions = actions + [new_position]
                            # If the new position is not visited yet or we found a new path with a lower cost to reach this position, add it to the queue
                            if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                                visited_costs[new_position] = new_cost
                                h = heuristic(new_position, end)
                                heapq.heappush(queue, (g + h, new_cost, new_actions, new_position))
                                break
    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the destination
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
