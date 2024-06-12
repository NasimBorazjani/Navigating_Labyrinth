
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 1),)
    goal_state = (10, 8)
    num_rows = 12
    num_cols = 12
    grid = [[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
            [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0])

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[-1] == goal_state:
            return actions

        if len(state) <= 5:
            row, col = state[-1]
            for d_row, d_col in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    new_state = state + ((new_row, new_col),)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the Manhattan distance between the current position and the goal position
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the shortest path between two points is a straight line
    # The heuristic is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    h = 0
    for pos in state:
        h += abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    return h


print(a_star())
