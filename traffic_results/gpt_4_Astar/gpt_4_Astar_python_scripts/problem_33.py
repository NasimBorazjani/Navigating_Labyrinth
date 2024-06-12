
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (2, 10)
   goal_state = (5, 2)
   # Define the map of the city
   city_map = np.array([[16, 10, 'x', 16, 1, 12, 6, 12, 3, 7, 'x'],
                        ['x', 16, 10, 9, 12, 19, 7, 10, 12, 13, 7],
                        [5, 'x', 9, 'x', 5, 16, 16, 8, 'x', 16, 8],
                        ['x', 4, 14, 'x', 'x', 'x', 'x', 'x', 'x', 7, 18],
                        [13, 12, 16, 14, 'x', 2, 4, 2, 'x', 6, 3],
                        ['x', 11, 20, 'x', 'x', 'x', 1, 'x', 'x', 9, 'x'],
                        ['x', 'x', 8, 10, 'x', 'x', 3, 1, 'x', 'x', 6],
                        ['x', 2, 9, 'x', 8, 13, 'x', 'x', 'x', 12, 11],
                        [12, 'x', 2, 'x', 'x', 1, 6, 'x', 15, 'x', 1],
                        [3, 'x', 'x', 'x', 17, 'x', 18, 4, 1, 'x', 'x'],
                        ['x', 'x', 6, 'x', 'x', 12, 'x', 'x', 'x', 15, 12]])
   num_rows = city_map.shape[0]
   num_cols = city_map.shape[1]
   # Define the districts
   districts = [range(0, 2), range(2, 5), range(5, 11)]


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
           # Check if the new state would be valid, ie the new workshop must be within the bounds of the city map and not be closed
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
                   h = heuristic(new_state, goal_state, city_map)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop, multiplied by the minimum travel time in the city map
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes he can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the minimum travel time, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   min_travel_time = np.min(city_map[city_map != 'x'].astype(int))
   h = (abs(state[0] - goal[0]) + abs(state[1] - goal[1])) * min_travel_time
   return h


print(a_star())
