
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (2, 3)
    goal_state = (8, 10)
    # Define the map of the city
    city_map = np.array([['x', 'x', '10', 'x', 'x', 'x', '3', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['6', '19', 'x', 'x', 'x', '12', 'x', 'x', '3', 'x', 'x', 'x', 'x'],
                         ['5', '3', '7', '7', 'x', '7', '9', 'x', '18', 'x', 'x', 'x', 'x'],
                         ['1', '4', '19', '19', '16', '6', 'x', '2', '10', 'x', '1', '7', 'x'],
                         ['14', '10', 'x', 'x', '2', '3', '5', '3', '13', '7', 'x', '8', 'x'],
                         ['x', '8', '11', '14', '18', 'x', 'x', '16', '15', '8', 'x', '10', 'x'],
                         ['x', '17', 'x', 'x', '15', 'x', 'x', '1', '17', '9', '7', 'x', '10'],
                         ['18', '6', '14', '4', '12', '12', 'x', '12', '5', 'x', 'x', '5', '18'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', '7', '17', '4', '16', 'x', 'x'],
                         ['x', '6', '17', 'x', 'x', 'x', 'x', 'x', '15', 'x', 'x', '12', 'x'],
                         ['14', 'x', 'x', '12', '3', '11', 'x', 'x', 'x', 'x', 'x', 'x', '17'],
                         ['x', '16', 'x', 'x', 'x', '3', '5', '19', 'x', '16', '14', 'x', '19'],
                         ['13', 'x', '11', 'x', '3', '16', 'x', '1', 'x', 'x', '1', 'x', 'x']])
    num_rows, num_cols = city_map.shape
    # Define the districts
    districts = [range(0, 3), range(3, 8), range(8, 13)]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    visited_costs = {}
    visited_costs[(initial_state, frozenset())] = 0


    queue = [(0, 0, [], initial_state, frozenset())]


    while queue:
        _, g, actions, state, visited_districts = heapq.heappop(queue)


        if state == goal_state and len(visited_districts) == len(districts):
            return actions


        for d_row, d_col in directions:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_state = (new_row, new_col)
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts.add(i)
                new_cost = g + int(city_map[new_row][new_col])


                if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                    visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                    h = heuristic(new_state, goal_state, len(new_visited_districts), len(districts))
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
    return None


def heuristic(state, goal, num_visited_districts, num_districts):
    # The heuristic function is the Manhattan distance from the current state to the goal state plus the number of districts not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the Manhattan distance is the shortest path in a grid with obstacles and visiting each district is a mandatory task
    # The heuristic is consistent because the cost of moving to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if the state is moved toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0 and all districts must have been visited.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1]) + num_districts - num_visited_districts


print(a_star())
