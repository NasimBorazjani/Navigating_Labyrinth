
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((8, 1),)
    destination = (1, 9)
    grid = [[1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]]
    num_rows = 10
    num_cols = 10

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[-1] == destination:
            return actions

        if len(state) <= 4:
            current_position = state[-1]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_position = (current_position[0] + i, current_position[1] + j)
                    if 0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and grid[new_position[0]][new_position[1]] == 0:
                        new_state = state + (new_position,)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_position, destination)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_position], new_state))
    return None


def heuristic(current_position, destination):
    # The heuristic is the Manhattan distance between the current position and the destination
    # This heuristic is admissible because it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    return abs(current_position[0] - destination[0]) + abs(current_position[1] - destination[1])


print(a_star())
