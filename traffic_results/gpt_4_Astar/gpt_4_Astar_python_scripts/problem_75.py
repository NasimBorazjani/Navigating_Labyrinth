
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (7, 1)
    goal_state = (2, 10)
    # Define the map of the city as a 2d tuple
    city_map = (('x', '9', '4', '8', 'x', 'x', '4', 'x', '8', '12', 'x', 'x', '14'),
                ('17', 'x', '3', 'x', '6', 'x', '12', '2', 'x', 'x', 'x', '5', '19'),
                ('x', '8', '8', 'x', '5', 'x', '15', '14', '14', '3', '10', '12', '3'),
                ('4', 'x', '16', 'x', 'x', '11', '12', 'x', 'x', '6', '5', '18', '19'),
                ('x', '4', '9', '17', 'x', 'x', 'x', '13', '4', '7', 'x', '2', '16'),
                ('3', '6', 'x', 'x', 'x', '10', '5', 'x', '18', '10', '9', '20', '4'),
                ('x', 'x', 'x', '14', '18', 'x', 'x', 'x', 'x', '16', 'x', 'x', '4'),
                ('14', '12', 'x', '4', '12', '11', '19', 'x', '3', '2', 'x', '13', 'x'),
                ('19', '6', '2', '18', 'x', 'x', '8', '7', '1', '12', '19', 'x', 'x'),
                ('x', '9', '16', '17', '5', '12', '19', '8', 'x', '3', '10', 'x', 'x'),
                ('x', '10', '3', 'x', '14', '16', '2', '16', '4', '10', '18', '15', 'x'),
                ('15', '5', '5', 'x', '13', 'x', '3', '7', 'x', '4', '1', '17', '15'),
                ('5', '2', '6', 'x', 'x', 'x', 'x', '8', '16', 'x', 'x', 'x', 'x'))
    num_rows = len(city_map)
    num_cols = len(city_map[0])
    # Define the districts of the city
    districts = [range(0, 3), range(3, 8), range(8, 13)]
    # Define the set of workshops visited in each district
    visited_districts = [set() for _ in range(len(districts))]


    visited_costs = {}
    visited_costs[(initial_state, tuple(visited_districts))] = 0


    queue = [(0, 0, [], (initial_state, visited_districts))]


    while queue:
        _, g, actions, (state, visited_districts) = heapq.heappop(queue)


        if state == goal_state and all(visited_districts[i] for i in range(len(districts))):
            return actions


        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_state = (new_row, new_col)
                new_visited_districts = [set(district) for district in visited_districts]
                for i, district in enumerate(districts):
                    if new_row in district:
                        new_visited_districts[i].add(new_state)
                new_visited_districts = tuple(new_visited_districts)
                new_cost = g + int(city_map[new_row][new_col])


                if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                    visited_costs[(new_state, new_visited_districts)] = new_cost
                    h = heuristic(new_state, goal_state, new_visited_districts, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], (new_state, new_visited_districts)))
    return None


def heuristic(state, goal, visited_districts, districts):
    # The heuristic function can be the Manhattan distance from the current state to the goal state, plus the sum of the minimum travel times from the current state to the nearest unvisited workshop in each district
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes the car can move in a straight line to the goal state and to the nearest unvisited workshop in each district, ignoring the constraints on the movement of the car and the presence of closed workshops
    # The heuristic is consistent because the cost of moving from one state to a neighboring state is always greater than or equal to 1 (the minimum travel time), which is exactly the decrease in the Manhattan distance if the car moves toward the goal state or the nearest unvisited workshop in a district, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the Manhattan distance of the goal state from itself is 0 and all workshops in each district have been visited.
    h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    for i in range(len(districts)):
        if not visited_districts[i]:
            min_travel_time = min(abs(state[0] - workshop[0]) + abs(state[1] - workshop[1]) for workshop in districts[i])
            h += min_travel_time
    return h


print(a_star())
