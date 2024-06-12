
import heapq
import math


def a_star():
    # Define the initial state of the grid and the goal state
    initial_state = ((8, 6),)
    goal_state = (0, 0)
    grid = [[0, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 0, 0]]
    
    # Encoding other variables given in the problem statement
    num_rows = 9
    num_cols = 9
    num_diagonal_jumps = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = []
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If Alex reaches the goal state, return the actions taken
        if state[-1] == goal_state and len(state) == num_diagonal_jumps + 1:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        current_position = state[-1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_position = (current_position[0] + i, current_position[1] + j)
                # Check if the new position is within the bounds of the grid and is not a broken trampoline
                if 0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and grid[new_position[0]][new_position[1]] == 0:
                    # Calculate the cost of moving to the new position
                    new_cost = g + 1
                    new_state = state + (new_position,)
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_position, goal_state)
                        heappush(queue, (new_cost + h, new_cost, actions + [new_position], new_state))
    
    return None


def heuristic(current_position, goal_position):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal state
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])


print(a_star())
