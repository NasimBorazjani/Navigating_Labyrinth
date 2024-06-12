
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'),
        ('x', 6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'),
        ('x', 'x', 11, 5, 'x', 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4),
        ('x', 3, 'x', 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x'),
        (4, 1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'),
        (8, 5, 17, 'x', 'x', 1, 'x', 'x', 'x', 19, 14, 2, 1, 'x', 'x'),
        (11, 9, 'x', 'x', 14, 'x', 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16),
        ('x', 'x', 2, 'x', 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x'),
        ('x', 'x', 'x', 16, 'x', 7, 'x', 'x', 'x', 7, 11, 18, 9, 17),
        (13, 19, 13, 'x', 18, 'x', 14, 'x', 14, 14, 'x', 'x', 20, 15, 15),
        ('x', 'x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 'x', 6, 11, 'x'),
        (5, 'x', 7, 'x', 15, 'x', 'x', 19, 1, 'x', 'x', 10, 'x', 'x', 18),
        (11, 19, 'x', 18, 'x', 5, 'x', 19, 16, 'x', 'x', 13, 'x', 'x', 5),
        (8, 16, 6, 13, 1, 'x', 14, 4, 'x', 'x', 'x', 1, 'x', 'x', 5),
        ('x', 19, 5, 'x', 'x', 'x', 12, 5, 9, 16, 11, 9, 14, 'x', 'x')
    )
    num_rows = 15
    num_cols = 15
    districts = [(0, 3), (4, 7), (8, 14)]
    start = (8, 13)
    end = (3, 3)


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
                # The cost of moving to a new position is the travel time at that position
                new_cost = g + initial_state[new_row][new_col]
              
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    # Check if Ben has visited at least 1 workshop in each district on the path to the destination
                    if all(any(district[0] <= new_position[0] <= district[1] for district in districts) for new_position in actions + [new_position]):
                        # Calculate the heuristic cost to the destination
                        h = heuristic(new_position, end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))
    return None


def heuristic(current, destination):
    # The heuristic is the Manhattan distance between the current position and the destination
    return abs(current[0] - destination[0]) + abs(current[1] - destination[1])


print(a_star())
