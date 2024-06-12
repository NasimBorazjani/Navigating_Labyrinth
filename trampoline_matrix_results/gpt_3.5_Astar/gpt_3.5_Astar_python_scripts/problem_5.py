
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 0),)
    goal_state = (5, 7)
    num_rows = 9
    num_cols = 9
    grid = [[0, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 1]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[-1] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                # Check if the new state would be valid, ie the trampoline must not be broken and the jump must be diagonal
                new_row = state[-1][0] + d_row
                new_col = state[-1][1] + d_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0 and (d_row != 0 and d_col != 0):
                    new_state = state + ((new_row, new_col),)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, goal):
    # The heuristic function calculates the Manhattan distance between the current position and the goal position
    # This heuristic is admissible because the Manhattan distance is the minimum number of moves required to reach the goal state
    # The heuristic is consistent because moving diagonally is always more costly than moving horizontally or vertically, so the heuristic estimate is always less than or equal to the actual cost to reach the goal state
    h = 0
    current_position = state[-1]
    h += abs(current_position[0] - goal[0]) + abs(current_position[1] - goal[1])
    return h


print(a_star())
