
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((13, 13, 16, 8, 'x', 19, 1, 18, 13, 8, 'x', 7, 'x'),
                     ('x', 13, 'x', 15, 'x', 12, 20, 1, 13, 19, 4, 17, 'x'),
                     ('x', 12, 9, 11, 13, 12, 2, 12, 19, 5, 19, 16, 8),
                     ('x', 12, 18, 19, 'x', 7, 'x', 12, 3, 2, 'x', 16, 11),
                     ('x', 7, 'x', 'x', 8, 13, 15, 3, 1, 'x', 15, 15, 'x'),
                     (11, 9, 'x', 16, 2, 10, 1, 2, 16, 1, 'x', 10, 12),
                     ('x', 'x', 9, 9, 7, 'x', 6, 'x', 'x', 10, 7, 2, 'x'),
                     ('x', 13, 10, 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
                     (11, 14, 'x', 'x', 'x', 'x', 4, 8, 'x', 'x', 18, 'x', 'x'),
                     (13, 14, 'x', 10, 'x', 'x', 16, 'x', 'x', 'x', 'x', 'x', 'x'),
                     ('x', 'x', 16, 'x', 10, 'x', 17, 'x', 12, 'x', 10, 'x', 5),
                     (9, 'x', 10, 'x', 19, 16, 'x', 14, 16, 12, 15, 7, 'x'),
                     (1, 'x', 8, 10, 14, 'x', 6, 9, 'x', 'x', 8, 11, 11))
    num_rows = 13
    num_cols = 13
    districts = {1: [(0, 1), (1, 1)], 2: [(2, 1), (5, 1)], 3: [(6, 1), (12, 1)]}
    start = (3, 12)
    end = (6, 2)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [], start)]


    while queue:
        _, g, actions, current = heapq.heappop(queue)


        # If Ben reaches the destination, return the path taken
        if current == end:
            return actions


        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            # Check if the new position is within the bounds of the city map and is not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                # Calculate the cost of moving to the new position
                new_cost = g + initial_state[new_row][new_col]
              
                # Check if the new position is in a different district than the current position
                current_district = get_district(current, districts)
                new_district = get_district(new_position, districts)
                if current_district != new_district:
                    new_cost += 10  # Add additional cost for changing districts
                  
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))
    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the destination
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


def get_district(position, districts):
    # Helper function to determine the district of a given position
    for district, coords in districts.items():
        if position in coords:
            return district
    return None


print(a_star())
