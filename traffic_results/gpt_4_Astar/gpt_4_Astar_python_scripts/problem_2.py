
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (2, 2)
    goal_state = (5, 8)
    # Define the map of the city
    city_map = np.array([['x', 13, 9, 'x', 'x', 16, 6, 18, 7],
                         ['x', 3, 11, 'x', 'x', 5, 7, 'x', 19],
                         [8, 'x', 2, 5, 6, 12, 9, 10, 7],
                         [12, 1, 6, 20, 19, 18, 12, 'x', 14],
                         [16, 5, 10, 3, 'x', 'x', 'x', 1, 9],
                         ['x', 3, 'x', 'x', 'x', 'x', 'x', 'x', 4],
                         [7, 10, 'x', 1, 'x', 'x', 17, 'x', 8],
                         ['x', 5, 'x', 'x', 'x', 17, 'x', 9, 'x'],
                         [13, 16, 8, 15, 'x', 2, 'x', 1, 2]])
    # Define the districts
    districts = [(0, 1), (2, 4), (5, 8)]
    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Define the visited costs
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [initial_state], initial_state, [False, False, False])]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, visited_districts = heapq.heappop(queue)
        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts):
            return path
        # Generate all possible actions from the current state
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid
            if (0 <= new_state[0] < city_map.shape[0] and
                0 <= new_state[1] < city_map.shape[1] and
                city_map[new_state] != 'x'):
                # Calculate the cost so far
                new_cost = g + int(city_map[new_state])
                # Update the visited districts
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if district[0] <= new_state[0] <= district[1]:
                        new_visited_districts[i] = True
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, path + [new_state], new_state, new_visited_districts))
    return None


print(a_star())
