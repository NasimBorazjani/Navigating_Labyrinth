
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 10),)
    goal_state = (9, 2)
    num_rows = 11
    num_cols = 11
    grid = [[0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[-1] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        current_position = state[-1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_position = (current_position[0] + i, current_position[1] + j)
                # Check if the new position is within the bounds of the grid and is not a broken trampoline
                if 0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and grid[new_position[0]][new_position[1]] == 0:
                    # Calculate the number of diagonal jumps made so far
                    diagonal_jumps = sum(1 for pos in state if abs(pos[0] - current_position[0]) == 1 and abs(pos[1] - current_position[1]) == 1)
                    # Check if the number of diagonal jumps is less than 3
                    if diagonal_jumps < 3:
                        new_state = state + (new_position,)
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_position, goal_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_position], new_state))

    return None


def heuristic(current_position, goal_position):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])


print(a_star())
