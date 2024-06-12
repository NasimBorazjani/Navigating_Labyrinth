
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((4, 0),)
    goal_state = (12, 12)
    num_rows = 13
    num_cols = 13
    grid = [[1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[-1] == goal_state and len(state) == 5:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[-1][0] + i
                new_col = state[-1][1] + j
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    new_state = state + ((new_row, new_col),)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    
    return None


def heuristic(state, goal):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the Manhattan distance
    h = abs(state[-1][0] - goal[0]) + abs(state[-1][1] - goal[1])
    return h


print(a_star())
