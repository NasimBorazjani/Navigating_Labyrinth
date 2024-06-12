
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (8, 13)
   goal_state = (3, 3)
   # Define the map of the city
   city_map = np.array([['x', 9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'],
                        ['x', 6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'],
                        ['x', 'x', 11, 5, 'x', 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4],
                        ['x', 3, 'x', 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x'],
                        [4, 1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'],
                        [8, 5, 17, 'x', 'x', 1, 'x', 'x', 'x', 19, 14, 2, 1, 'x', 'x'],
                        [11, 9, 'x', 'x', 14, 'x', 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16],
                        ['x', 'x', 2, 'x', 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x'],
                        ['x', 'x', 'x', 16, 'x', 7, 'x', 'x', 'x', 'x', 7, 11, 18, 9, 17],
                        [13, 19, 13, 'x', 18, 'x', 14, 'x', 14, 14, 'x', 'x', 20, 15, 15],
                        ['x', 'x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 'x', 6, 11, 'x'],
                        [5, 'x', 7, 'x', 15, 'x', 'x', 19, 1, 'x', 'x', 10, 'x', 'x', 18],
                        [11, 19, 'x', 18, 'x', 5, 'x', 19, 16, 'x', 'x', 13, 'x', 'x', 5],
                        [8, 16, 6, 13, 1, 'x', 14, 4, 'x', 'x', 'x', 1, 'x', 'x', 5],
                        ['x', 19, 5, 'x', 'x', 'x', 12, 5, 9, 16, 11, 9, 14, 'x', 'x']])
   num_rows = city_map.shape[0]
   num_cols = city_map.shape[1]
   # Define the districts
   districts = [range(0, 4), range(4, 8), range(8, 15)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == 3:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
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
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor workshop is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself is 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # If Ben has not visited all districts yet, add a penalty to the heuristic
   if len(visited_districts) < 3:
       h += 10
   return h


print(a_star())
