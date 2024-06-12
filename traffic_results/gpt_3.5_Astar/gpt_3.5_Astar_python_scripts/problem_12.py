
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((19, 'x', 17, 14, 3, 'x', 10, 5, 2),
                     ('x', 'x', 1, 'x', 'x', 'x', 19, 7, 1),
                     (16, 12, 'x', 3, 19, 2, 14, 1, 14),
                     ('x', 1, 16, 'x', 12, 3, 13, 'x', 3),
                     ('x', 'x', 7, 19, 10, 'x', 5, 'x', 19),
                     (5, 'x', 'x', 6, 14, 'x', 'x', 10, 12),
                     ('x', 'x', 'x', 'x', 18, 'x', 'x', 15, 12),
                     ('x', 'x', 16, 8, 'x', 3, 4, 'x', 'x'),
                     ('x', 'x', 'x', 16, 'x', 'x', 8, 14, 7))
    num_rows = 9
    num_cols = 9
    districts = {1: [(0, 3), (1, 6), (2, 8), (3, 5)],
                 2: [(4, 0), (4, 2), (4, 6), (4, 8)],
                 3: [(5, 1), (6, 7), (7, 2), (7, 5), (8, 3), (8, 7)]}
    start = (3, 1)
    end = (5, 8)


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
                # Calculate the cost of moving to the new position
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                # The cost of the new state is the sum of the travel times from the start to the current position
                new_cost = sum(initial_state[row][col] for row, col in new_path)
              
                if new_path[-1] not in visited_costs or new_cost < visited_costs[new_path[-1]]:
                    visited_costs[new_path[-1]] = new_cost
                    h = heuristic(new_path, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_path[-1]], new_path))
    return None


def heuristic(path, districts):
    # The heuristic function calculates the sum of the distances from the current position to the nearest workshop in each district that has not been visited yet
    # This heuristic is admissible because it underestimates the cost to reach the goal, as it only considers the distance to the nearest workshop in each district
    # The heuristic is consistent because the cost of moving to the nearest workshop in each district is always less than or equal to the actual cost of reaching that workshop
    # The cost of the goal state is 0, as Ben has visited at least 1 workshop in each district and has reached the destination workshop
    h = 0
    for district, positions in districts.items():
        if not any(pos in path for pos in positions):
            min_distance = math.inf
            for pos in positions:
                distance = abs(pos[0] - path[-1][0]) + abs(pos[1] - path[-1][1])
                min_distance = min(min_distance, distance)
            h += min_distance
    return h


print(a_star())
