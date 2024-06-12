
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((12, 9))
    destination = (3, 1)
    num_rows = 13
    num_cols = 13
    grid = [[0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1])
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == destination:
            return actions

        x, y = state
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = x + i, y + j
                if 0 <= new_x < num_rows and 0 <= new_y < num_cols and grid[new_x][new_y] == 0 and (i != 0 or j != 0):
                    new_state = (new_x, new_y)
                    new_cost = g + math.sqrt(i**2 + j**2)
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, destination)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_x, new_y)], new_state))
    return None


def heuristic(state, destination):
    # The heuristic is the Euclidean distance between the current state and the destination
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the shortest path between two points is a straight line
    # The heuristic is consistent because the cost of moving from one state to a neighboring state is always 1, which is exactly the decrease in the Euclidean distance
    x1, y1 = state
    x2, y2 = destination
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


print(a_star())
