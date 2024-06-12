
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 2)
    goal_state = (7, 13)
    # Define the map of the city
    city_map = np.array([['x', 2, 'x', 12, 3, 8, 'x', 1, 5, 'x', 'x', 14, 'x', 5, 'x'],
                         [5, 'x', 'x', 9, 19, 10, 10, 'x', 'x', 14, 16, 'x', 'x', 17, 'x'],
                         [7, 4, 7, 18, 2, 7, 16, 'x', 7, 'x', 9, 'x', 'x', 6, 'x'],
                         [9, 'x', 14, 'x', 'x', 14, 7, 9, 18, 11, 14, 8, 13, 14, 15],
                         [8, 4, 'x', 17, 'x', 7, 15, 'x', 'x', 19, 'x', 10, 'x', 12, 13],
                         [7, 11, 5, 6, 'x', 13, 'x', 'x', 15, 4, 9, 17, 19, 6, 8],
                         [13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 4, 10, 'x', 7, 7, 17, 9],
                         ['x', 'x', 6, 'x', 'x', 17, 12, 11, 'x', 'x', 'x', 10, 15, 14, 'x'],
                         [16, 'x', 5, 19, 'x', 19, 'x', 4, 11, 16, 'x', 'x', 12, 'x', 'x'],
                         ['x', 'x', 14, 'x', 'x', 19, 'x', 'x', 4, 13, 7, 'x', 'x', 'x', 8],
                         ['x', 4, 'x', 13, 7, 14, 'x', 'x', 2, 15, 9, 11, 'x', 'x', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 19, 'x', 6, 2, 'x', 'x', 'x', 4, 7, 'x'],
                         [17, 12, 10, 3, 5, 18, 'x', 'x', 'x', 11, 'x', 19, 13, 'x', 'x'],
                         [1, 'x', 5, 'x', 17, 'x', 17, 'x', 7, 18, 'x', 'x', 8, 'x', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 2, 9, 'x', 10, 3, 'x', 'x', 15, 2]])
    # Define the districts
    districts = [range(0, 3), range(3, 7), range(7, 15)]
    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Define the visited costs
    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state, frozenset())]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and all districts have been visited
        if state == goal_state and len(visited_districts) == len(districts):
            return actions
        # Generate all possible actions from the current state
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state[0], new_state[1]] != 'x'):
                # Calculate the new cost
                new_cost = g + int(city_map[new_state[0], new_state[1]])
                # Update the visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_state[0] in district:
                        new_visited_districts.add(i)
                # If the new state is unvisited or we found a new path with a lower cost to reach this state
                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    # Calculate the heuristic
                    h = heuristic(new_state, goal_state)
                    # Add the new state to the queue
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal):
    # The heuristic function can be the Manhattan distance between the current state and the goal state
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
