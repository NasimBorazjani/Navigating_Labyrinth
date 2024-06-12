
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (1, 3)
    goal_state = (6, 10)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([['x', 'x', 'x', '6', '9', 'x', 'x', '10', '14', '7', '3', '12'],
                         ['x', '11', 'x', '3', '14', '16', '17', '1', '4', '14', '8', '16'],
                         ['3', 'x', 'x', 'x', '6', '1', '18', '16', 'x', '6', '3', '11'],
                         ['x', 'x', '11', '4', '8', 'x', 'x', '1', '3', '9', '8', '7'],
                         ['x', 'x', '3', 'x', 'x', 'x', '8', '14', '18', 'x', 'x', '18'],
                         ['4', '1', 'x', 'x', 'x', '14', 'x', 'x', 'x', '3', '4', '20'],
                         ['1', 'x', 'x', 'x', '14', '19', '15', 'x', 'x', '3', '16', '15'],
                         ['x', 'x', '6', '18', 'x', 'x', '16', '1', 'x', '3', 'x', '11'],
                         ['x', '3', 'x', '15', 'x', '19', '10', 'x', 'x', 'x', 'x', 'x'],
                         ['x', '9', 'x', 'x', 'x', 'x', '17', '17', 'x', '16', 'x', '13'],
                         ['x', 'x', '8', 'x', 'x', '1', 'x', 'x', 'x', '19', '19', '1'],
                         ['x', '3', '9', 'x', 'x', 'x', 'x', '1', 'x', '10', '11', '8']])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 2), range(2, 6), range(6, 12)]
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
                    h = heuristic(new_state, goal_state, city_map, districts, new_visited_districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal, city_map, districts, visited_districts):
    # An admissible and consistent heuristic for this problem is the straight-line distance (Euclidean distance) from the current workshop to the goal workshop, multiplied by the minimum travel time in the city
    # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the decrease in the straight-line distance, if the workshop is moved toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
    # The heuristic also adds the minimum travel time in the city for each unvisited district, as Ben must visit at least one workshop in each district
    h = np.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2) * int(np.min(city_map[city_map != 'x']))
    h += len(districts) * int(np.min(city_map[city_map != 'x'])) - len(visited_districts) * int(np.min(city_map[city_map != 'x']))
    return h


print(a_star())
