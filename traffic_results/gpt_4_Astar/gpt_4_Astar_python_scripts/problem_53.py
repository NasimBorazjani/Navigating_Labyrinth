
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 3)
    goal_state = (7, 11)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[18, 'x', 'x', 14, 5, 'x', 'x', 5, 18, 'x', 3, 'x'],
                         ['x', 'x', 'x', 9, 2, 2, 'x', 15, 14, 12, 'x', 18],
                         ['x', 'x', 3, 16, 3, 9, 'x', 16, 'x', 14, 'x', 17],
                         ['x', 'x', 'x', 19, 7, 20, 'x', 'x', 11, 4, 'x', 4],
                         [7, 'x', 8, 11, 'x', 1, 15, 5, 'x', 'x', 11, 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 6, 11, 'x', 'x', 'x', 8],
                         ['x', 15, 2, 'x', 'x', 18, 'x', 1, 16, 15, 6, 5],
                         ['x', 4, 18, 8, 9, 'x', 'x', 17, 20, 13, 'x', 10],
                         ['x', 16, 'x', 'x', 19, 'x', 17, 'x', 13, 11, 14, 2],
                         [12, 'x', 11, 'x', 3, 'x', 5, 3, 'x', 13, 17, 6],
                         [14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 16],
                         [12, 'x', 'x', 'x', 12, 'x', 10, 'x', 18, 14, 8, 'x']])
    num_rows = city_map.shape[0]
    num_cols = city_map.shape[1]
    # Define the districts of the city
    districts = [(0, 3), (4, 6), (7, 11)]
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
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state] != 'x'):
                # The new state is valid, generate the new state
                # Check if the new state is in a new district
                new_visited_districts = set(visited_districts)
                for i, district in enumerate(districts):
                    if district[0] <= new_state[0] <= district[1]:
                        new_visited_districts.add(i)
                new_visited_districts = frozenset(new_visited_districts)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + city_map[new_state]


                if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                    visited_costs[(new_state, new_visited_districts)] = new_cost
                    h = heuristic(new_state, goal_state, len(districts) - len(new_visited_districts))
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal, num_districts_left):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop, plus the minimum travel time to cross a district times the number of districts left to visit
    # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move to any workshop in the city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0 and all districts must have been visited.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1]) + num_districts_left
    return h


print(a_star())
