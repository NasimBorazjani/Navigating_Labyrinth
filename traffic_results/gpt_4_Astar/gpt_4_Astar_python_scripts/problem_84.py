
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (9, 10)
    goal_state = (2, 3)
    # Define the map of the city
    city_map = np.array([['x', 10, 16, 12, 'x', 'x', 'x', 'x', 18, 18, 10, 'x', 'x', 19],
                         [7, 'x', 'x', 11, 5, 13, 6, 'x', 'x', 'x', 'x', 'x', 8, 14],
                         ['x', 15, 6, 20, 4, 9, 16, 9, 16, 'x', 11, 'x', 'x', 9],
                         [1, 16, 'x', 'x', 'x', 6, 15, 1, 10, 10, 9, 4, 'x', 4],
                         ['x', 'x', 'x', 1, 12, 'x', 12, 17, 'x', 'x', 13, 'x', 'x', 2],
                         ['x', 'x', 9, 'x', 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 10, 11],
                         [7, 'x', 7, 12, 'x', 'x', 'x', 2, 2, 8, 10, 8, 'x', 'x'],
                         [3, 3, 'x', 16, 11, 'x', 4, 6, 'x', 'x', 4, 17, 13, 16],
                         [4, 15, 'x', 'x', 'x', 'x', 'x', 'x', 11, 19, 16, 'x', 'x', 'x'],
                         [10, 5, 17, 'x', 2, 'x', 'x', 3, 10, 3, 12, 'x', 8, 'x'],
                         ['x', 17, 12, 'x', 'x', 'x', 6, 2, 13, 'x', 'x', 'x', 'x', 'x'],
                         ['x', 10, 'x', 'x', 15, 'x', 'x', 'x', 8, 'x', 3, 'x', 'x', 19],
                         [1, 7, 'x', 'x', 16, 'x', 'x', 'x', 3, 15, 10, 12, 6, 8],
                         ['x', 'x', 'x', 'x', 9, 'x', 'x', 'x', 7, 'x', 'x', 'x', 'x', 8]])
    # Define the districts
    districts = [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Define the visited costs
    visited_costs = {}
    visited_costs[(initial_state, frozenset([districts[initial_state[0]]]))] = 0
    # Define the queue
    queue = [(0, 0, [initial_state], initial_state, frozenset([districts[initial_state[0]]]))]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, visited_districts = heapq.heappop(queue)
        # If the current state is the goal state and all districts have been visited
        if state == goal_state and len(visited_districts) == 3:
            return path
        # Generate all possible actions from the current state
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state[0], new_state[1]] != 'x'):
                new_visited_districts = visited_districts | {districts[new_state[0]]}
                new_cost = g + int(city_map[new_state[0], new_state[1]])
                if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                    visited_costs[(new_state, new_visited_districts)] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, path + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # The heuristic function can be the Manhattan distance between the current state and the goal state
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
