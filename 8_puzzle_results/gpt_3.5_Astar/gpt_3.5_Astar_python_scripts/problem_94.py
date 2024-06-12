
import heapq
import math
import numpy as np


def a_star():
    # Define the initial state of the puzzle as a 2d tuple
    initial_state = ((98, 30, 85, 44, 59, 40),
                     (56, 68, 50, 61, 47, 15),
                     (37, 48, 24, 81, 22, '_'))

    # Define the goal state of the puzzle
    goal_state = ((98, 85, 68, 61, 59, 50),
                  (56, 48, 44, 40, 37, 30),
                  (24, 22, 15, '_', '_', '_'))

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 6:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = tuple(tuple(row) for row in new_state)

                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost using the Manhattan distance between the current state and the goal state
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[new_row][new_col]], new_state))

    return None


def heuristic(state, goal_state):
    # Calculate the Manhattan distance between the current state and the goal state
    h = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                # Find the position of the current number in the goal state
                goal_pos = [(k, l) for k, row in enumerate(goal_state) for l, cell in enumerate(row) if cell == state[i][j]][0]
                # Calculate the Manhattan distance and add it to the heuristic cost
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])

    return h


print(a_star())
