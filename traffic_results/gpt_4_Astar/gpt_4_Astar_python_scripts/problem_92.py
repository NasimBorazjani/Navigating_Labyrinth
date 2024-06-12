
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (7, 14)
   goal_state = (2, 4)
   # Define the map of the city
   city_map = np.array([[15, 1, 'x', 3, 'x', 9, 15, 8, 17, 'x', 'x', 6, 'x', 12, 3],
                        ['x', 'x', 'x', 14, 'x', 7, 18, 6, 14, 2, 19, 15, 'x', 'x', 'x'],
                        [4, 3, 'x', 10, 8, 4, 16, 13, 6, 'x', 18, 10, 14, 'x', 'x'],
                        ['x', 'x', 'x', 10, 'x', 14, 10, 7, 'x', 'x', 'x', 4, 2, 19, 3],
                        [5, 'x', 10, 'x', 18, 12, 20, 15, 'x', 'x', 11, 11, 1, 10, 19],
                        [8, 'x', 13, 'x', 'x', 'x', 16, 7, 3, 'x', 'x', 2, 18, 11, 'x'],
                        [12, 'x', 15, 'x', 'x', 6, 'x', 'x', 'x', 'x', 18, 3, 14, 3, 6],
                        ['x', 6, 13, 19, 19, 'x', 7, 12, 18, 5, 'x', 1, 4, 18, 11],
                        [5, 'x', 18, 'x', 12, 4, 3, 7, 'x', 16, 1, 'x', 16, 2, 'x'],
                        ['x', 'x', 'x', 'x', 18, 'x', 'x', 14, 15, 1, 'x', 'x', 9, 'x', 'x'],
                        ['x', 13, 'x', 7, 7, 'x', 'x', 16, 10, 'x', 'x', 'x', 'x', 8, 'x'],
                        ['x', 'x', 19, 18, 8, 18, 'x', 'x', 12, 'x', 13, 'x', 17, 12, 7],
                        ['x', 'x', 'x', 'x', 7, 7, 13, 17, 'x', 'x', 'x', 'x', 'x', 9, 5],
                        [9, 'x', 14, 'x', 9, 'x', 8, 'x', 'x', 'x', 17, 4, 12, 12, 12],
                        [8, 1, 11, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 2, 16, 'x', 15]])
   num_rows = city_map.shape[0]
   num_cols = city_map.shape[1]
   # Define the districts
   districts = [range(0, 3), range(3, 7), range(7, 15)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], (initial_state, frozenset()))]


   while queue:
       _, g, actions, (state, visited_districts) = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == len(districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new cell must be within the bounds of the city map and not be a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + city_map[new_row][new_col]
               # Check if the new state is in a new district
               new_visited_districts = visited_districts.copy()
               for i, district in enumerate(districts):
                   if new_row in district and i not in visited_districts:
                       new_visited_districts.add(i)
                       break


               if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                   visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], (new_state, frozenset(new_visited_districts))))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben can't move through closed workshops and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben is moved toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
