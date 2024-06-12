
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[36, 16, 48], [86, '_', 13], [89, 31, 37]]
    goal_state = [[86, 89, 48], [37, 36, 31], [16, 13, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = np.argwhere(np.array(state) == '_')[0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = str(new_state)

                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state))

    return None


def heuristic(state, goal_state):
    # The heuristic function is the sum of the Manhattan distances of each tile from its goal position
    state = eval(state)
    goal_state = eval(goal_state)

    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                tile = state[i][j]
                goal_pos = np.argwhere(np.array(goal_state) == tile)[0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])

    return h


solution = a_star()
if solution:
    print([int(action[-1]) for action in solution])
else:
    print("No solution found.")
