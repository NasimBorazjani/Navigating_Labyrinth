
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (7, 8)
   goal_state = (2, 1)
   # Define the map of the city
   city_map = np.array([['x', 18, 'x', 5, 'x', 6, 5, 'x', 6, 17, 'x'],
                        ['x', 'x', 1, 5, 9, 13, 'x', 2, 'x', 'x', 2],
                        ['x', 17, 12, 'x', 'x', 'x', 5, 'x', 'x', 17, 'x'],
                        [9, 3, 13, 8, 'x', 7, 'x', 'x', 4, 2, 'x'],
                        [11, 17, 'x', 10, 'x', 'x', 'x', 'x', 17, 15, 11],
                        ['x', 10, 10, 14, 9, 7, 1, 5, 'x', 'x', 7],
                        ['x', 5, 6, 12, 8, 9, 4, 'x', 'x', 4, 9],
                        [11, 'x', 4, 13, 14, 'x', 12, 17, 13, 'x', 'x'],
                        ['x', 8, 'x', 19, 11, 7, 7, 19, 15, 14, 7],
                        [11, 8, 'x', 11, 10, 16, 'x', 'x', 9, 'x', 5],
                        [9, 4, 'x', 'x', 1, 11, 14, 'x', 'x', 'x', 10]])
   num_rows = city_map.shape[0]
   num_cols = city_map.shape[1]
   # Define the districts
   districts = [range(0, 3), range(3, 8), range(8, 11)]


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
           # Check if the new state would be valid, ie the new workshop must be within the bounds of the city map and not be a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
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
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # Add a penalty for each district not yet visited
   h += len(districts) - len(visited_districts)
   return h


print(a_star())
