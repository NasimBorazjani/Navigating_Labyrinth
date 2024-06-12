
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (1, 8)
   goal_state = (4, 1)
   # Define the map of the city
   city_map = np.array([[13, 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x', 6],
                        ['x', 'x', 'x', 8, 10, 'x', 17, 'x', 15, 14],
                        ['x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11],
                        ['x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'],
                        [18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5],
                        [11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1],
                        ['x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'],
                        ['x', 8, 15, 17, 16, 6, 'x', 3, 'x', 10],
                        [3, 'x', 'x', 'x', 8, 9, 10, 'x', 6, 'x'],
                        [6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x']])
   num_rows = 10
   num_cols = 10
   # Define the districts
   districts = {1: range(0, 2), 2: range(2, 5), 3: range(5, 10)}


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == len(districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new cell must be within the bounds of the city map and not be a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + int(city_map[new_row][new_col])
               # Update the set of visited districts
               new_visited_districts = visited_districts.copy()
               for district, rows in districts.items():
                   if new_row in rows:
                       new_visited_districts.add(district)


               if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                   visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                   h = heuristic(new_state, goal_state, city_map)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current cell to the goal cell, multiplied by the minimum travel time in the city map
   # The heuristic relaxes the constraint that Ben can only move to a neighboring cell and presumes he can move directly to the goal cell
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always greater than or equal to the minimum travel time, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal cell, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal cell from itself would be 0.
   h = (abs(state[0] - goal[0]) + abs(state[1] - goal[1])) * np.min(city_map[city_map != 'x'].astype(int))
   return h


print(a_star())
