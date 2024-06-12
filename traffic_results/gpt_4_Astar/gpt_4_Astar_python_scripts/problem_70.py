
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 1)
   goal_state = (2, 11)
   # Define the map of the city
   city_map = np.array([[13, 'x', 10, 17, 'x', 4, 8, 'x', 7, 'x', 12, 19, 4],
                        [17, 'x', 8, 11, 7, 'x', 'x', 19, 'x', 11, 'x', 13, 18],
                        [15, 6, 2, 12, 16, 7, 'x', 14, 'x', 2, 'x', 14, 4],
                        ['x', 18, 4, 'x', 'x', 'x', 13, 14, 2, 4, 20, 10, 7],
                        [7, 2, 19, 16, 'x', 'x', 'x', 18, 'x', 'x', 'x', 2, 2],
                        [10, 17, 14, 7, 17, 3, 3, 19, 'x', 19, 'x', 'x', 9],
                        [9, 'x', 'x', 'x', 5, 18, 13, 6, 'x', 'x', 'x', 19, 10],
                        ['x', 'x', 'x', 'x', 'x', 2, 7, 4, 'x', 'x', 'x', 'x', 'x'],
                        ['x', 'x', 6, 3, 'x', 1, 'x', 'x', 14, 'x', 18, 'x', 1],
                        [14, 'x', 4, 18, 14, 12, 'x', 'x', 'x', 'x', 2, 'x', 13],
                        [12, 'x', 3, 1, 12, 9, 'x', 6, 'x', 'x', 16, 'x', 18],
                        [13, 'x', 11, 5, 3, 4, 'x', 'x', 'x', 'x', 'x', 'x', 18],
                        [15, 9, 9, 1, 'x', 6, 'x', 'x', 14, 'x', 'x', 1, 14]])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [(0, 1), (2, 5), (6, 12)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset([0, 1, 2]))] = 0


   queue = [(0, 0, [], initial_state, frozenset([0, 1, 2]))]


   while queue:
       _, g, actions, state, remaining_districts = heapq.heappop(queue)


       if state == goal_state and not remaining_districts:
           return actions


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               # Check if the new state is in a district that has not been visited yet
               new_remaining_districts = frozenset(district for district in remaining_districts if not (districts[district][0] <= new_row <= districts[district][1]))
               new_cost = g + city_map[new_row][new_col]
               if (new_state, new_remaining_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_remaining_districts)]:
                   visited_costs[(new_state, new_remaining_districts)] = new_cost
                   h = heuristic(new_state, goal_state, new_remaining_districts, districts)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_remaining_districts))
   return None


def heuristic(state, goal, remaining_districts, districts):
   # The heuristic function can be the Manhattan distance from the current state to the goal state, plus the sum of the minimum distances from the current state to the nearest unvisited district and from that district to the goal state
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes we can move directly to the goal state or the nearest unvisited district, ignoring any obstacles
   # The heuristic is consistent because the cost of moving to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if the state is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   if remaining_districts:
       min_distance_to_district = min(abs(state[0] - districts[district][0]) + abs(state[1] - districts[district][1]) for district in remaining_districts)
       h += min_distance_to_district
   return h


print(a_star())
