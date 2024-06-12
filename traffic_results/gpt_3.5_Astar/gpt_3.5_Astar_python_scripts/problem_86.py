
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((0, 0, 11, 16, 0, 0, 0, 0, 4, 0, 14, 5, 0, 0),
                      (3, 1, 13, 0, 0, 14, 11, 0, 0, 15, 12, 15, 0, 0),
                      (17, 15, 17, 10, 11, 0, 7, 1, 1, 14, 0, 9, 0, 0),
                      (8, 0, 0, 13, 2, 12, 0, 8, 0, 0, 9, 13, 19, 5),
                      (4, 0, 2, 3, 8, 0, 0, 17, 0, 0, 16, 10, 0, 0),
                      (0, 0, 0, 0, 3, 13, 14, 16, 18, 11, 4, 19, 20, 0),
                      (0, 11, 0, 0, 3, 10, 8, 9, 18, 7, 1, 14, 0, 6),
                      (11, 0, 12, 11, 0, 11, 10, 3, 10, 12, 15, 0, 11, 0),
                      (0, 0, 4, 18, 0, 0, 13, 0, 14, 10, 0, 8, 0, 17),
                      (0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 18, 19, 18),
                      (19, 4, 0, 2, 14, 2, 0, 9, 0, 10, 7, 17, 4, 12),
                      (13, 2, 0, 0, 18, 5, 0, 11, 0, 0, 0, 18, 0, 0),
                      (0, 0, 13, 1, 13, 0, 2, 0, 0, 0, 0, 0, 14, 0),
                      (0, 12, 0, 0, 0, 0, 0, 0, 19, 0, 0, 9, 1, 0))

    num_rows = 14
    num_cols = 14
    districts = [(0, 3), (4, 6), (7, 13)]
    start = (3, 0)
    end = (5, 12)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end:
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 0:
                new_cost = g + initial_state[new_row][new_col]
                new_pos = (new_row, new_col)

                if any(start <= new_row <= end for start, end in districts) and (new_pos not in visited_costs or new_cost < visited_costs[new_pos]):
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_pos], new_pos))

    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
