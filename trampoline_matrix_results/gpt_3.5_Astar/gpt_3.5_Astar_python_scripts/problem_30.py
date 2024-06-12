
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 9),)
    goal_state = (7, 3)
    num_rows = 10
    num_cols = 10
    grid = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[-1] == goal_state and len([pos for pos in state if pos[0] != pos[1]]) == 3:
            return actions

        x, y = state[-1]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < num_rows and 0 <= new_y < num_cols and grid[new_x][new_y] == 0:
                    new_state = state + ((new_x, new_y),)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_x, new_y)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the Manhattan distance from the current position to the goal position
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    h = 0
    for pos in state:
        h += abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    return h


print(a_star())
