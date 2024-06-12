
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[92, 72, 91, 79, 62, 24], [93, 67, 65, 63, 83, 74], [41, 34, 29, 27, 58, '_']]
    goal_state = [[92, 91, 83, 79, 74, 67], [65, 63, 62, 58, 41, 34], [33, 32, 31, 29, 27, 24]]

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
                # Create a new state by swapping the empty spot with the neighboring tile
                new_state = [row[:] for row in state]
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
                new_state = str(new_state)
                # The cost of the new state is the number on the tile that was swapped with the empty spot
                new_cost = g + new_state[new_row][new_col]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[new_row][new_col]], new_state))

    return None


def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the number of misplaced tiles in the current state compared to the goal state
    # This heuristic relaxes the constraint that only the empty spot can be moved, as it considers the number of misplaced tiles
    # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
    # It is consistent because moving a tile closer to its correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
    h = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h


print(a_star())
