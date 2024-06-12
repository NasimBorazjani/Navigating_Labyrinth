
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 7), (12, 1))
    num_rows = 13
    num_cols = 13
    grid = [[1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]]
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex has made exactly 4 diagonal jumps, check if he has reached the destination
        if len(actions) == 4 and state[1] == (12, 1):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[1][0] + i
                new_col = state[1][1] + j
                # Check if the new position is within the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Check if the move is diagonal
                    if abs(i) == 1 and abs(j) == 1:
                        # Ensure Alex has made exactly 4 diagonal jumps
                        if len([action for action in actions if abs(action[0] - new_row) == 1 and abs(action[1] - new_col) == 1]) == 3:
                            new_state = (state[1], (new_row, new_col))
                            new_cost = g + 1
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                h = heuristic(new_state)
                                heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
                    else:
                        new_state = (state[1], (new_row, new_col))
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state):
    # The heuristic is the Manhattan distance from the current position to the destination
    h = abs(state[1][0] - 12) + abs(state[1][1] - 1)
    return h


print(a_star())
