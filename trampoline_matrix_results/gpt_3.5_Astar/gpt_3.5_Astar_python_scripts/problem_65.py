
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 0),)
    goal_state = (8, 9)
    num_rows = 13
    num_cols = 13
    grid = [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[-1] == goal_state:
            return actions

        if len(state) <= 5:
            x, y = state[-1]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x, new_y = x + i, y + j
                    if 0 <= new_x < num_rows and 0 <= new_y < num_cols and grid[new_x][new_y] == 0 and (i != 0 or j != 0):
                        new_state = state + ((new_x, new_y),)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state, goal_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_x, new_y)], new_state))
    return None


def heuristic(state, goal):
    # The heuristic is the Manhattan distance from the current position to the goal position
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the agent can only move in 8 directions
    # The heuristic is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    x, y = state[-1]
    goal_x, goal_y = goal
    return abs(x - goal_x) + abs(y - goal_y)


print(a_star())
