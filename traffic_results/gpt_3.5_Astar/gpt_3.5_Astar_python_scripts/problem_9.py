
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((6, 9, 19, 'x', 5, 9, 'x', 15, 'x'),
                     (8, 10, 16, 'x', 'x', 'x', 5, 11, 4),
                     (5, 11, 20, 1, 14, 16, 7, 1, 5),
                     (10, 5, 3, 5, 12, 8, 'x', 'x', 2),
                     (16, 15, 15, 14, 'x', 13, 10, 'x', 10),
                     (6, 4, 7, 13, 'x', 'x', 'x', 'x', 13),
                     ('x', 1, 6, 3, 'x', 'x', 17, 9, 5),
                     ('x', 11, 'x', 9, 'x', 5, 7, 'x', 'x'),
                     ('x', 'x', 'x', 18, 'x', 2, 'x', 'x', 12))
    num_rows = 9
    num_cols = 9
    districts = {1: [(0, 1), (1, 1)], 2: [(2, 1), (3, 1), (4, 1), (2, 0), (3, 0), (4, 0)], 3: [(5, 1), (6, 1), (7, 1), (8, 1), (5, 0), (6, 0), (7, 0), (8, 0)]}
    start = (1, 8)
    end = (4, 0)


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
                visited_districts = set()
                for district, workshops in districts.items():
                    if current in workshops:
                        visited_districts.add(district)
                    if new_position in workshops:
                        visited_districts.add(district)
                if len(visited_districts) == 3:
                    # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of unvisited positions
                    if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                        visited_costs[new_position] = new_cost
                        h = heuristic(new_position, end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))
    return None


def heuristic(current, end):
    # The heuristic function is the Manhattan distance between the current position and the destination
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
