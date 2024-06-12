
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 0)
    goal_state = (9, 7)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[16, 'x', 5, 6, 'x', 14, 12, 'x', 'x', 'x', 6, 'x'],
                         [17, 'x', 'x', 'x', 5, 'x', 5, 7, 'x', 'x', 8, 'x'],
                         [3, 19, 'x', 'x', 'x', 'x', 18, 'x', 13, 7, 'x', 'x'],
                         [13, 'x', 4, 'x', 'x', 8, 7, 4, 'x', 15, 'x', 'x'],
                         [5, 17, 18, 12, 3, 'x', 14, 2, 4, 18, 'x', 1],
                         [4, 10, 1, 19, 10, 'x', 'x', 17, 'x', 17, 16, 4],
                         [7, 'x', 16, 'x', 'x', 1, 3, 'x', 13, 13, 'x', 'x'],
                         ['x', 'x', 9, 1, 7, 18, 16, 3, 'x', 4, 'x', 'x'],
                         [2, 'x', 13, 10, 'x', 4, 'x', 'x', 'x', 'x', 'x', 12],
                         ['x', 'x', 'x', 18, 8, 4, 'x', 11, 'x', 14, 18, 'x'],
                         ['x', 19, 2, 'x', 2, 6, 5, 18, 'x', 5, 'x', 'x'],
                         ['x', 2, 'x', 7, 'x', 'x', 8, 7, 'x', 11, 16, 'x']])
    num_rows = city_map.shape[0]
    num_cols = city_map.shape[1]
    # Define the districts in the city
    districts = [(0, 3), (4, 8), (9, 11)]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0


    queue = [(0, 0, [], initial_state, frozenset())]


    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)


        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions


        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the city and not a closed workshop
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state[0]][new_state[1]] != 'x'):
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + city_map[new_state[0]][new_state[1]]
                # Check if the new state is in a new district
                new_visited_districts = set(visited_districts)
                for i, district in enumerate(districts):
                    if district[0] <= new_state[0] <= district[1]:
                        new_visited_districts.add(i)
                new_visited_districts = frozenset(new_visited_districts)


                if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                    visited_costs[(new_state, new_visited_districts)] = new_cost
                    h = heuristic(new_state, goal_state, visited_districts, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal_state, visited_districts, districts):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
    h = abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])
    # Add a penalty for each unvisited district
    h += len(districts) - len(visited_districts)
    return h


print(a_star())
