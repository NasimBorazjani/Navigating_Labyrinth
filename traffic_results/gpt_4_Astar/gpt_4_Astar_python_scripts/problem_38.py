
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (3, 6)
    goal_state = (8, 0)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([['x', 'x', 'x', '3', 'x', 'x', '16', 'x', '2', '16', '3'],
                         ['8', 'x', '8', '5', 'x', 'x', '10', 'x', '19', '4', 'x'],
                         ['x', 'x', '18', '1', '16', 'x', '9', '15', 'x', 'x', '11'],
                         ['x', 'x', '17', '16', '4', '19', '2', 'x', '1', '11', 'x'],
                         ['9', 'x', '5', '16', '18', 'x', 'x', '7', 'x', '18', '6'],
                         ['x', '15', '7', 'x', 'x', 'x', '19', '8', '9', '17', 'x'],
                         ['x', '15', '19', 'x', 'x', 'x', '6', '2', '6', 'x', '5'],
                         ['x', '12', '11', '3', '11', '4', 'x', 'x', 'x', '3', 'x'],
                         ['18', '12', '4', 'x', '3', '10', 'x', '3', 'x', '7', '14'],
                         ['15', '11', '12', 'x', '13', '2', 'x', 'x', '5', '14', 'x'],
                         ['x', 'x', '15', 'x', '16', '4', '10', '13', 'x', 'x', '4']])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 4), range(4, 8), range(8, 11)]
    # Define the directions in which Ben can move
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0


    queue = [(0, 0, [], initial_state, frozenset())]


    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)


        # Check if the current state is the goal state
        if state == goal_state and len(visited_districts) == len(districts):
            return actions


        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state would be valid, ie the new workshop must be within the bounds of the city and not be closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
                new_cost = g + int(city_map[new_row][new_col])
                # Update the set of visited districts
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts.add(i)


                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state, visited_districts, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal, visited_districts, districts):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
    # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    # Add a penalty for each district not yet visited
    h += len(districts) - len(visited_districts)
    return h


print(a_star())
