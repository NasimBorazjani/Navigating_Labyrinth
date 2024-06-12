
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 0)
    goal_state = (8, 9)
    # Define the map of the city
    city_map = np.array([[16, 9, 19, 14, 16, 19, 6, 'x', 'x', 'x', 16, 18, 'x'],
                         [19, 'x', 'x', 9, 9, 'x', 17, 16, 3, 'x', 'x', 14, 'x'],
                         ['x', 'x', 11, 'x', 5, 'x', 15, 15, 17, 10, 'x', 13, 5],
                         [2, 12, 9, 18, 7, 'x', 'x', 'x', 4, 'x', 10, 'x', 3],
                         [8, 9, 19, 1, 'x', 4, 8, 'x', 17, 6, 'x', 18, 'x'],
                         ['x', 6, 7, 9, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 5, 4, 12, 13, 13, 'x', 'x', 'x', 11, 'x', 5, 9],
                         ['x', 'x', 2, 20, 6, 11, 2, 'x', 'x', 'x', 10, 18, 'x'],
                         ['x', 'x', 1, 18, 1, 17, 2, 3, 10, 12, 11, 'x', 19],
                         ['x', 16, 3, 'x', 'x', 16, 3, 10, 19, 'x', 'x', 9, 'x'],
                         [10, 'x', 'x', 'x', 'x', 1, 10, 13, 'x', 'x', 13, 'x', 'x'],
                         ['x', 'x', 'x', 'x', 13, 'x', 1, 14, 'x', 10, 'x', 'x', 8],
                         ['x', 'x', 'x', 'x', 'x', 9, 2, 18, 19, 14, 10, 'x', 'x']])
    # Define the districts
    districts = [(0, 3), (4, 8), (9, 12)]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Define the visited costs
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state, [False, False, False])]

    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts):
            return actions

        # Generate all possible actions from the current state
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state[0]][new_state[1]] != 'x'):
                # Calculate the new cost
                new_cost = g + int(city_map[new_state[0]][new_state[1]])
                # Update the visited districts
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if district[0] <= new_state[0] <= district[1]:
                        new_visited_districts[i] = True
                # Check if the new state has been visited or if the new cost is lower than the previous cost
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic
                    h = heuristic(new_state, goal_state)
                    # Add the new state to the queue
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))

    return None


def heuristic(state, goal):
    # The heuristic function can be the Manhattan distance between the current state and the goal state
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
