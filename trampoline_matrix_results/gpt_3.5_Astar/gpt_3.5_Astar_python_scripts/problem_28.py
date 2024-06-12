
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((8, 0),)
    destination = (0, 6)
    grid = [[1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]]
    
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[0] == destination:
            return actions

        x, y = state[0]
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 10 and 0 <= new_y < 10 and grid[new_x][new_y] == 0:
                    new_state = ((new_x, new_y),)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, destination)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_x, new_y)], new_state))
    
    return None


def heuristic(state, destination):
    # The heuristic is the Manhattan distance between the current position and the destination
    # This heuristic is admissible because it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    x, y = state[0]
    dest_x, dest_y = destination
    return abs(x - dest_x) + abs(y - dest_y)


print(a_star())
