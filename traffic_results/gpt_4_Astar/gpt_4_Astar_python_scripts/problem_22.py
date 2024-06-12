
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (1, 0)
   goal_state = (5, 7)
   # Define the map of the city
   city_map = np.array([[2, 2, 3, 'x', 2, 10, 'x', 8, 6, 'x'],
                        [6, 11, 'x', 'x', 'x', 'x', 'x', 16, 'x', 7],
                        [17, 17, 7, 12, 13, 15, 5, 6, 10, 13],
                        [1, 15, 13, 3, 'x', 'x', 'x', 14, 'x', 9],
                        [14, 'x', 'x', 6, 15, 2, 12, 18, 'x', 18],
                        [11, 19, 1, 19, 10, 8, 'x', 14, 'x', 'x'],
                        [11, 'x', 'x', 'x', 3, 'x', 'x', 7, 'x', 2],
                        [16, 12, 'x', 'x', 'x', 5, 'x', 'x', 10, 'x'],
                        ['x', 11, 'x', 2, 12, 'x', 8, 'x', 8, 'x'],
                        ['x', 'x', 16, 'x', 'x', 'x', 16, 'x', 16, 12]])
   num_rows, num_cols = city_map.shape
   # Define the districts
   districts = [range(0, 2), range(2, 5), range(5, 10)]
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


       # Generate all possible actions from the current state, which includes moving in any of the 4 directions
       for d_row, d_col in directions:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state] != 'x'):
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + int(city_map[new_state])
               # Update the set of visited districts
               new_visited_districts = visited_districts.copy()
               for i, district in enumerate(districts):
                   if new_state[0] in district:
                       new_visited_districts.add(i)
              
               if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                   visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                   h = heuristic(new_state, goal_state, visited_districts, districts)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
   return None


def heuristic(state, goal, visited_districts, districts):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # Add a penalty for each district not yet visited
   h += len(districts) - len(visited_districts)
   return h


print(a_star())
