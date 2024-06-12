
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (6, 12)
    goal_state = (5, 0)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([['x', 'x', 'x', 'x', '9', '1', '14', 'x', 'x', 'x', '11', '15', '12'],
                         ['2', 'x', '18', 'x', '14', 'x', '11', '3', 'x', 'x', 'x', 'x', 'x'],
                         ['10', 'x', '3', 'x', 'x', 'x', '8', '6', 'x', '10', '9', '7', 'x'],
                         ['1', '18', '2', '6', 'x', 'x', '1', '5', 'x', 'x', '6', 'x', 'x'],
                         ['4', '14', '12', '3', '2', '2', '15', '8', '19', '3', '18', 'x', 'x'],
                         ['5', '6', '2', '2', '13', 'x', '7', '3', '12', 'x', '16', '10', '5'],
                         ['x', '2', '13', 'x', 'x', '9', '5', 'x', 'x', 'x', '7', '10', '11'],
                         ['17', '10', '3', '11', '4', 'x', 'x', '19', 'x', '5', 'x', 'x', '9'],
                         ['13', 'x', 'x', 'x', 'x', '9', '13', '4', '7', 'x', '13', '10', 'x'],
                         ['x', 'x', 'x', '9', 'x', '8', '8', '14', 'x', 'x', '19', 'x', 'x'],
                         ['6', 'x', 'x', 'x', 'x', 'x', '1', '11', 'x', '4', '13', 'x', 'x'],
                         ['x', 'x', 'x', '11', '11', 'x', '9', '16', '12', 'x', '6', 'x', '5'],
                         ['16', '19', '14', 'x', '5', '13', 'x', 'x', 'x', 'x', 'x', '13', 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts of the city
    districts = [range(0, 4), range(4, 6), range(6, 13)]
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


        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
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
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Ben can only move to a neighboring cell and presumes Ben can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
