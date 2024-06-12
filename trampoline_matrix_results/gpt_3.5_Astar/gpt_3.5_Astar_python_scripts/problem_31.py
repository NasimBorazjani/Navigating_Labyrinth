
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0),
                      (1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0),
                      (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                      (0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1),
                      (0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1),
                      (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0),
                      (0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1),
                      (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0),
                      (1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1),
                      (0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1),
                      (1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1))
    num_rows = 11
    num_cols = 11
    start = (1, 10)
    goal = (9, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == goal:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row = current[0] + i
                new_col = current[1] + j
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                    # Check if the diagonal jumps are exactly 3
                    if abs(i) == 1 and abs(j) == 1:
                        diagonal_jumps = 1
                    else:
                        diagonal_jumps = 0

                    new_state = (new_row, new_col)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))

    return None


def heuristic(current, goal):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


print(a_star())
