
import heapq
import numpy as np


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[12, 76, '_', 72, 53], [61, 97, 49, 65, 52], [89, 64, 22, 26, 13]]
    goal_state = [[97, 89, 76, 72, 65], [64, 61, 53, 52, 49], [26, 22, 13, 12, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = np.argwhere(np.array(state) == '_')[0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 5:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = str(new_state)
                # The cost so far is the number of actions taken
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost using the Manhattan distance
                    h = heuristic(new_state, goal_state)
                    heappush(queue, (g + h, g + 1, actions + [state[new_row][new_col]], new_state))

    return None


def heuristic(state, goal_state):
    # Calculate the Manhattan distance heuristic
    state = eval(state)
    goal_state = eval(goal_state)
    h = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                current_tile = state[i][j]
                goal_pos = np.argwhere(np.array(goal_state) == current_tile)[0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
