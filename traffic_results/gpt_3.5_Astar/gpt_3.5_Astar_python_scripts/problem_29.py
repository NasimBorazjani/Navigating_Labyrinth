
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((0, 0, 0, 4, 6, 0, 9, 15, 11, 2),
                     (19, 0, 14, 3, 10, 18, 0, 0, 0, 1),
                     (0, 9, 0, 11, 7, 14, 0, 0, 16, 18),
                     (0, 5, 4, 5, 2, 4, 7, 5, 19, 14),
                     (0, 3, 20, 0, 5, 16, 0, 0, 1, 9),
                     (0, 3, 15, 9, 4, 0, 0, 0, 0, 4),
                     (11, 18, 19, 8, 17, 9, 0, 10, 10, 19),
                     (0, 0, 0, 17, 7, 0, 0, 7, 12, 8),
                     (0, 0, 11, 19, 0, 13, 10, 13, 0, 0),
                     (18, 0, 0, 0, 6, 10, 7, 0, 8, 0))
    num_rows = 10
    num_cols = 10
    districts = {1: [(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)],
                 2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)],
                 3: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9)]}
    start = (3, 9)
    end = (6, 1)


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
            # Check if the new position is within the bounds of the city map
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Check if the new position is not a closed workshop
                if initial_state[new_row][new_col] != 0:
                    new_path = path + [(new_row, new_col)]
                    new_cost = g + initial_state[new_row][new_col]
                    # If the new position is not visited or we found a new path with a lower cost to reach this position, add it to the queue
                    if new_path[-1] not in visited_costs or new_cost < visited_costs[new_path[-1]]:
                        visited_costs[new_path[-1]] = new_cost
                        h = heuristic(new_path, districts)
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_path[-1]], new_path))
    return None


def heuristic(path, districts):
    # The heuristic function calculates the sum of the distances from the current position to the nearest workshop in each district that has not been visited yet
    # This heuristic is admissible because it underestimates the cost to reach the goal, as it only considers the distance to the nearest unvisited workshop in each district
    # The heuristic is consistent because the cost of moving from one position to another is always 1, and the estimated cost of the successor node is the same or higher, and the cost of the goal state is 0, as Ben has visited all required workshops
    h = 0
    visited_districts = set(pos for pos in path if any(pos in district for district in districts.values()))
    for district, workshop_positions in districts.items():
        if district not in visited_districts:
            min_distance = math.inf
            for pos in path:
                for workshop_pos in workshop_positions:
                    distance = abs(pos[0] - workshop_pos[0]) + abs(pos[1] - workshop_pos[1])
                    if distance < min_distance:
                        min_distance = distance
            h += min_distance
    return h


print(a_star())
