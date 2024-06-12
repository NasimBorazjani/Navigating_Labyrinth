
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 14, 15, 10, 'x', 14, 'x', 'x', 18, 6, 'x', 'x', 4),
                     (6, 'x', 'x', 'x', 1, 'x', 15, 'x', 'x', 2, 'x', 17, 'x'),
                     ('x', 4, 'x', 17, 3, 14, 4, 2, 'x', 3, 'x', 11, 'x'),
                     (6, 6, 'x', 19, 'x', 13, 'x', 11, 13, 6, 3, 'x', 'x'),
                     (3, 10, 11, 'x', 'x', 4, 4, 1, 19, 'x', 'x', 'x', 17),
                     (8, 'x', 'x', 8, 11, 18, 17, 19, 18, 'x', 1, 1, 'x'),
                     (14, 14, 1, 19, 6, 'x', 19, 19, 18, 9, 'x', 12, 18),
                     (17, 6, 8, 'x', 1, 14, 19, 13, 'x', 'x', 9, 'x', 3),
                     (16, 4, 'x', 'x', 'x', 9, 5, 'x', 'x', 'x', 18, 'x', 'x'),
                     ('x', 'x', 10, 'x', 18, 'x', 1, 'x', 'x', 12, 9, 8, 3),
                     ('x', 13, 17, 'x', 'x', 'x', 5, 8, 1, 'x', 1, 10, 'x'),
                     (10, 11, 'x', 12, 'x', 6, 11, 'x', 9, 9, 15, 'x', 10),
                     (5, 15, 1, 'x', 8, 5, 'x', 6, 'x', 9, 18, 'x', 'x'))
    num_rows = 13
    num_cols = 13
    districts = {1: (0, 3), 2: (4, 7), 3: (8, 12)}
    start_workshop = (3, 8)
    end_workshop = (8, 0)

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[end_workshop[0]][end_workshop[1]] != 'x':
            return actions

        # Generate all possible actions from the current state, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = start_workshop[0] + d_row
            new_col = start_workshop[1] + d_col
            # Check if the new position is within the bounds of the city map
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
                # Generate the new state
                new_state = [list(row[:]) for row in state]
                new_state[start_workshop[0]][start_workshop[1]] = 'x'
                new_state[new_row][new_col] = state[start_workshop[0]][start_workshop[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost so far is the sum of travel times from the start workshop to the current workshop
                new_cost = g + int(state[start_workshop[0]][start_workshop[1]])

                # Check if the new state is unvisited or we found a new path with a lower cost to reach this state
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Check if the new workshop is in a different district than the previous workshop
                    for district, (start, end) in districts.items():
                        if start <= new_row <= end and start <= start_workshop[0] <= end:
                            break
                    if district not in [1, 2, 3]:
                        continue
                    heapq.heappush(queue, (g + heuristic(new_state, end_workshop, district), new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, end_workshop, district):
    # The heuristic is the Manhattan distance from the current workshop to the destination workshop in the same district
    # This heuristic is admissible as it never overestimates the cost to reach the goal state
    # The heuristic is consistent because the cost of moving from one workshop to another is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward the destination workshop, otherwise the estimated cost of the successor node is the same or higher
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 'x':
                h += abs(i - end_workshop[0]) + abs(j - end_workshop[1])
    return h


print(a_star())
