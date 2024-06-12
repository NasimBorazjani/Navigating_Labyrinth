
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (5, 2)
    goal_state = (2, 10)
    # Define the map of the city
    city_map = np.array([['x', 'x', '13', 'x', 'x', '7', 'x', '13', '3', 'x', '13'],
                         ['10', '4', 'x', '4', '12', '2', 'x', '3', '4', 'x', '15'],
                         ['x', '3', 'x', 'x', '15', '9', 'x', 'x', '18', '17', '14'],
                         ['5', 'x', 'x', 'x', '3', 'x', '11', 'x', '17', '9', '17'],
                         ['8', '3', '13', 'x', '5', '7', '8', '17', '7', 'x', 'x'],
                         ['x', 'x', '13', '2', '2', '11', '6', '8', 'x', 'x', 'x'],
                         ['x', '1', '9', '6', '5', '13', '16', '1', '7', '5', 'x'],
                         ['4', 'x', '13', 'x', '10', '18', '3', 'x', 'x', '19', '19'],
                         ['x', 'x', 'x', '2', '5', '9', '13', 'x', '7', '1', 'x'],
                         ['x', 'x', '7', 'x', 'x', '5', '19', 'x', 'x', 'x', 'x'],
                         ['x', 'x', 'x', '6', 'x', '19', 'x', 'x', 'x', 'x', '1']])
    # Define the districts
    districts = [0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2]
    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, frozenset([districts[initial_state[0]]]))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state], (initial_state, frozenset([districts[initial_state[0]]])))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, (state, visited_districts) = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == 3:
            return path

        # Generate all possible actions from the current state
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state[0], new_state[1]] != 'x'):
                new_visited_districts = visited_districts.union([districts[new_state[0]]])
                new_cost = g + int(city_map[new_state[0], new_state[1]])
                if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                    visited_costs[(new_state, new_visited_districts)] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, path + [new_state], (new_state, new_visited_districts)))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
