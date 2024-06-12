
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (7, 7)
   goal_state = (1, 2)
   # Define the map of the city as a 2d numpy array
   city_map = np.array([[10, 14, 4, 16, 'x', 17, 5, 'x', 'x'],
                        [5, 20, 16, 3, 1, 8, 'x', 16, 19],
                        [1, 'x', 5, 13, 3, 15, 19, 15, 'x'],
                        ['x', 16, 13, 20, 'x', 8, 'x', 'x', 'x'],
                        ['x', 16, 'x', 17, 11, 1, 'x', 15, 'x'],
                        [10, 'x', 14, 11, 5, 7, 12, 'x', 5],
                        [7, 'x', 15, 'x', 15, 8, 3, 6, 7],
                        ['x', 12, 14, 'x', 'x', 'x', 16, 3, 13],
                        [19, 5, 10, 'x', 'x', 'x', 9, 7, 14]])
   num_rows = city_map.shape[0]
   num_cols = city_map.shape[1]
   # Define the districts of the city
   districts = [(0, 1), (2, 6), (7, 8)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == len(districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new workshop must be within the bounds of the city and not be closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + city_map[new_row][new_col]
               # Update the set of visited districts
               new_visited_districts = visited_districts.copy()
               for i, district in enumerate(districts):
                   if district[0] <= new_row <= district[1]:
                       new_visited_districts.add(i)


               if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                   visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                   h = heuristic(new_state, goal_state, city_map)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop, multiplied by the minimum travel time in the city
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes he can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   h = (abs(state[0] - goal[0]) + abs(state[1] - goal[1])) * np.min(city_map[city_map != 'x'])
   return h


print(a_star())
