
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 10)
    goal_state = (6, 1)
    # Define the map of the city
    city_map = np.array([['x', 'x', 17, 12, 12, 10, 9, 9, 18, 'x', 1],
                         ['x', 8, 'x', 9, 'x', 'x', 18, 5, 1, 12, 14],
                         [2, 19, 4, 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x'],
                         [17, 8, 6, 'x', 'x', 10, 15, 'x', 'x', 'x', 13],
                         ['x', 'x', 'x', 9, 17, 'x', 'x', 'x', 'x', 12, 17],
                         ['x', 20, 3, 1, 14, 8, 9, 20, 10, 8, 8],
                         [18, 19, 4, 12, 3, 1, 'x', 'x', 20, 6, 3],
                         [4, 6, 9, 'x', 8, 10, 'x', 'x', 6, 9, 6],
                         [15, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 4, 'x'],
                         ['x', 'x', 'x', 4, 'x', 'x', 'x', 13, 'x', 'x', 'x'],
                         ['x', 3, 'x', 'x', 'x', 'x', 1, 'x', 'x', 5, 13]])
    # Define the districts
    districts = [range(0, 4), range(4, 6), range(6, 11)]
    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, [False]*3)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, visited_districts = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state and all(visited_districts):
            return actions

        # Generate all possible actions from the current state, which includes moving in any of the 4 directions
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
            if (0 <= new_state[0] < city_map.shape[0] and 0 <= new_state[1] < city_map.shape[1] and
                    city_map[new_state[0]][new_state[1]] != 'x'):
                # The cost so far is the sum of the travel times
                new_cost = g + city_map[new_state[0]][new_state[1]]
                # Update the visited districts
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if new_state[0] in district:
                        new_visited_districts[i] = True

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes there are no obstacles (closed workshops) in the path
    # The heuristic is consistent because the cost of moving to a neighboring state is always greater than or equal to 1 (the minimum travel time), which is exactly the decrease in the Manhattan distance, if the state is moved toward the goal state
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
