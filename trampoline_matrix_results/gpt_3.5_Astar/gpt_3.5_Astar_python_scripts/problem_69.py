
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((12, 0),)
    destination = (3, 8)
    grid = [[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]]
    
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
                if 0 <= new_x < 13 and 0 <= new_y < 13 and grid[new_x][new_y] == 0:
                    new_state = ((new_x, new_y),)
                    new_cost = g + math.sqrt(dx**2 + dy**2)
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = math.sqrt((new_x - destination[0])**2 + (new_y - destination[1])**2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_x, new_y)], new_state))
    return None


print(a_star())
