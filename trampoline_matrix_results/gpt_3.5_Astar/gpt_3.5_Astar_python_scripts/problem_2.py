
import heapq
import math


def a_star():
    # Define the initial state of the grid and the goal state
    initial_state = ((0, 4),)
    goal_state = (8, 0)
    grid = [[1, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0]]
  
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If Alex reaches the goal state, return the actions taken
        if state[-1] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
        current_position = state[-1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_position = (current_position[0] + i, current_position[1] + j)
                # Check if the new position is within the bounds of the grid and is not a broken trampoline
                if 0 <= new_position[0] < 9 and 0 <= new_position[1] < 9 and grid[new_position[0]][new_position[1]] == 0:
                    # Calculate the cost of moving to the new position
                    new_cost = g + 1
                    new_state = state + (new_position,)
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost based on the Euclidean distance to the goal state
                        h = math.sqrt((new_position[0] - goal_state[0]) ** 2 + (new_position[1] - goal_state[1]) ** 2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_position], new_state))
    return None


print(a_star())
