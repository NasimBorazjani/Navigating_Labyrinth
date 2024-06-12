
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (5, 2)
    goal_state = (9, 13)
    # Define the map of the city as a 2d tuple
    city_map = (('x', 'x', 'x', 'x', '9', 'x', '14', '17', 'x', '13', '3', 'x', '13', '10', '18'),
                ('1', 'x', '11', '12', '14', '13', '8', 'x', '5', '7', 'x', 'x', 'x', 'x', 'x'),
                ('3', 'x', 'x', '18', '11', '16', 'x', 'x', 'x', 'x', '1', 'x', '15', '12', '10'),
                ('x', '10', 'x', '3', '2', '15', '14', 'x', 'x', 'x', '17', 'x', '6', '1', 'x'),
                ('8', '10', 'x', 'x', 'x', 'x', '1', '19', '6', 'x', '17', '2', 'x', 'x', 'x'),
                ('x', '6', '15', '2', '17', '2', '11', '5', '9', 'x', '12', '15', 'x', 'x', '16'),
                ('x', 'x', '8', 'x', '14', 'x', '13', '20', '17', '12', '19', '9', 'x', 'x', 'x'),
                ('13', '10', '1', '4', '11', '3', '15', 'x', 'x', '3', '14', '20', 'x', '6', 'x'),
                ('x', '11', '16', '9', '19', '18', '12', '2', 'x', 'x', '1', '10', 'x', 'x', 'x'),
                ('x', '13', '18', '18', '7', 'x', 'x', 'x', 'x', '18', '5', '6', 'x', '7', '3'),
                ('x', 'x', 'x', '18', '6', '16', '10', '18', '9', '19', 'x', '3', '5', '3', '4'),
                ('14', '18', '4', '1', '17', 'x', '7', 'x', '3', '16', '11', 'x', '17', '11', '1'),
                ('x', 'x', '12', '16', 'x', '14', '9', 'x', 'x', 'x', '13', '1', 'x', 'x', '19'),
                ('19', 'x', '3', 'x', '8', 'x', 'x', 'x', '3', 'x', 'x', 'x', '17', '9', '8'),
                ('15', 'x', '2', '8', '9', '13', 'x', '14', 'x', '6', 'x', '19', 'x', 'x', '5'))
    num_rows = 15
    num_cols = 15
    # Define the districts of the city
    districts = [range(0, 5), range(5, 10), range(10, 15)]
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
            # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city and the workshop is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                # Generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the travel time to the new workshop, as the task is to minimize the travel time
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
    # Thus the heuristic reports a lower estimate on the travel time to reach the goal workshop and is admissible
    # The heuristic is consistent because the travel time to move to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated travel time of the successor workshop is the same or higher, and the heuristic estimate for the goal workshop is 0, as the distance of the goal workshop from itself would be 0.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    # Add a penalty for each district not yet visited
    h += (len(districts) - len(visited_districts)) * 10
    return h


print(a_star())
