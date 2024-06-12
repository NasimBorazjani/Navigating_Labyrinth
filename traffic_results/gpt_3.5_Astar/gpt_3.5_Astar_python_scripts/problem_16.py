
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 'x', 'x', 16, 1, 13, 17, 7, 14, 'x'),
                     ('x', 10, 'x', 12, 'x', 13, 'x', 8, 19, 4),
                     (9, 13, 'x', 13, 'x', 'x', 15, 'x', 'x', 16),
                     (3, 8, 'x', 16, 12, 'x', 'x', 'x', 'x', 13),
                     (13, 'x', 1, 15, 18, 8, 'x', 10, 'x', 'x'),
                     (8, 1, 2, 14, 'x', 8, 'x', 4, 'x', 11),
                     (14, 13, 15, 'x', 16, 'x', 13, 2, 'x', 19),
                     ('x', 4, 10, 'x', 'x', 16, 'x', 11, 'x', 'x'),
                     ('x', 14, 'x', 'x', 'x', 'x', 'x', 18, 6, 18),
                     ('x', 3, 2, 6, 7, 'x', 'x', 9, 8, 5))
    num_rows = 10
    num_cols = 10
    districts = {1: [(0, 3), (0, 4), (1, 0), (1, 2), (1, 5), (2, 0), (2, 3), (2, 6), (2, 9), (3, 0), (3, 1), (3, 3), (3, 9)],
                 2: [(4, 0), (4, 2), (4, 5), (5, 0), (5, 3), (5, 7), (5, 9)],
                 3: [(6, 0), (6, 1), (6, 2), (6, 4), (6, 6), (6, 8), (7, 2), (7, 4), (7, 6), (7, 8), (8, 1), (8, 3), (8, 8), (8, 9), (9, 0), (9, 2), (9, 3), (9, 4), (9, 7), (9, 9)]}
    start = (5, 1)
    end = (3, 9)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], [start])]

    while queue:
        _, g, actions, path = heapq.heappop(queue)
        current_position = path[-1]

        if current_position == end:
            return actions

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (current_position[0] + move[0], current_position[1] + move[1])

            if 0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and initial_state[new_position[0]][new_position[1]] != 'x' and new_position not in path:
                new_path = path + [new_position]
                new_cost = g + int(initial_state[new_position[0]][new_position[1]])

                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    h = heuristic(new_position, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_path))

    return None

def heuristic(current_position, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # If the current position is in a district, the heuristic is the Manhattan distance to the nearest workshop in the same district
    if current_position in districts[1]:
        nearest_workshop = min(districts[1], key=lambda x: abs(x[0] - current_position[0]) + abs(x[1] - current_position[1]))
    elif current_position in districts[2]:
        nearest_workshop = min(districts[2], key=lambda x: abs(x[0] - current_position[0]) + abs(x[1] - current_position[1]))
    elif current_position in districts[3]:
        nearest_workshop = min(districts[3], key=lambda x: abs(x[0] - current_position[0]) + abs(x[1] - current_position[1]))
    else:
        nearest_workshop = end

    return abs(current_position[0] - nearest_workshop[0]) + abs(current_position[1] - nearest_workshop[1])

print(a_star())
