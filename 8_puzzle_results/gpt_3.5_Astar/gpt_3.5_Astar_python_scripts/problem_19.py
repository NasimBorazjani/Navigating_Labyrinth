
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[89, 69, 35], [16, 14, 64], ['_', 23, 32]]
    goal_state = [[89, 69, 64], [35, 32, 23], [16, 14, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Find the position of the empty spot in the puzzle
        empty_spot = None
        for i in range(3):
            for j in range(3):
                if state[i][j] == '_':
                    empty_spot = (i, j)
                    break

        # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
        for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
            # Check if the new position is within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Generate the new state by swapping the empty spot with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[empty_spot[0]][empty_spot[1]] = new_state[new_row][new_col]
                new_state[new_row][new_col] = '_'
                new_state_str = str(new_state)
                # The cost of the new state is the number on the tile that was swapped with the empty spot
                new_cost = g + new_state[empty_spot[0]][empty_spot[1]]

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost using the Manhattan distance
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))

    return None


def heuristic(state, goal):
    # Calculate the Manhattan distance heuristic by summing the distances of each tile from its goal position
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                num = state[i][j]
                goal_pos = [(k, l) for k in range(3) for l in range(3) if goal[k][l] == num][0]
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


print(a_star())
