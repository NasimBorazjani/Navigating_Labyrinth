
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (4, 14)
   goal_state = (8, 3)
   # Define the map of the city
   city_map = np.array([[7, 6, 11, 'x', 'x', 'x', 19, 'x', 9, 15, 12, 8, 10, 15, 5],
                        [9, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 2, 11, 'x', 10],
                        [14, 5, 'x', 'x', 4, 4, 12, 'x', 18, 'x', 17, 11, 3, 18, 19],
                        [18, 17, 'x', 8, 'x', 'x', 9, 'x', 'x', 8, 19, 10, 'x', 'x', 'x'],
                        [7, 'x', 'x', 11, 4, 'x', 'x', 10, 1, 2, 3, 12, 8, 12, 15],
                        ['x', 3, 7, 8, 'x', 'x', 'x', 'x', 4, 16, 13, 19, 14, 10, 13],
                        [18, 1, 2, 'x', 16, 20, 5, 'x', 2, 4, 20, 12, 14, 18, 16],
                        [1, 'x', 1, 'x', 15, 19, 11, 9, 19, 16, 'x', 'x', 'x', 'x', 19],
                        ['x', 8, 'x', 1, 7, 'x', 2, 3, 'x', 'x', 'x', 'x', 1, 3, 'x'],
                        [6, 16, 'x', 3, 'x', 18, 'x', 2, 18, 'x', 'x', 16, 'x', 'x', 8],
                        ['x', 9, 'x', 5, 2, 'x', 'x', 'x', 'x', 17, 'x', 6, 18, 14, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 3, 'x', 10, 'x', 'x'],
                        ['x', 2, 15, 'x', 5, 15, 18, 8, 19, 'x', 'x', 'x', 'x', 'x', 10],
                        ['x', 'x', 4, 'x', 7, 2, 2, 'x', 19, 'x', 'x', 'x', 'x', 'x', 'x'],
                        [17, 'x', 'x', 'x', 5, 'x', 'x', 'x', 4, 1, 18, 'x', 9, 2, 8]])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [range(0, 5), range(5, 8), range(8, 15)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, [False, False, False])]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and all(visited_districts):
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
               # Update the visited districts
               new_visited_districts = visited_districts[:]
               for i, district in enumerate(districts):
                   if new_row in district:
                       new_visited_districts[i] = True
                       break


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move to the goal state directly
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
