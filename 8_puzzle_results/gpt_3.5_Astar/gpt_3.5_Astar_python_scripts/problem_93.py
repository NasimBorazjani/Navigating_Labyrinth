
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[94, 87, 69, 81, 4, 79], ['_', 35, 86, 61, 57, 75], [41, 18, 65, 9, 53, 55]]
    goal_state = [[94, 87, 81, 79, 75, 69], [65, 61, 57, 55, 53, 41], [35, 18, 9, 4, '_', 0]]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the current state
        empty_spot = [(i, j) for i in range(3) for j in range(6) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col

            # Check if the new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 6:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = str(new_state)
                # The cost of the new state is the number on the tile that was swapped with the empty spot
                new_cost = g + new_state[new_row][new_col]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [new_state[new_row][new_col]], new_state))
    return None


print(a_star())
