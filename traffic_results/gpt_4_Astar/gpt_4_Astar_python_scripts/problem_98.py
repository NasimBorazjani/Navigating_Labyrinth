
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (9, 3)
   goal_state = (4, 14)
   # Define the map of the city
   city_map = np.array([['x', 19, 4, 'x', 17, 11, 'x', 'x', 18, 7, 'x', 8, 20, 'x', 1],
                        ['x', 16, 'x', 1, 9, 1, 'x', 8, 16, 'x', 15, 7, 1, 'x', 'x'],
                        [7, 'x', 9, 9, 9, 'x', 18, 'x', 15, 13, 10, 'x', 19, 16, 9],
                        ['x', 'x', 'x', 6, 'x', 'x', 7, 10, 18, 17, 'x', 8, 9, 6, 5],
                        [4, 17, 'x', 'x', 19, 5, 20, 1, 15, 18, 'x', 'x', 5, 8, 2],
                        ['x', 'x', 'x', 3, 10, 19, 17, 20, 'x', 'x', 'x', 3, 'x', 5, 'x'],
                        ['x', 'x', 'x', 3, 8, 2, 'x', 'x', 7, 19, 'x', 'x', 1, 19, 9],
                        ['x', 19, 16, 6, 5, 19, 'x', 'x', 'x', 12, 'x', 3, 8, 10, 'x'],
                        [13, 2, 'x', 18, 'x', 'x', 5, 'x', 'x', 'x', 13, 1, 'x', 'x', 6],
                        [19, 8, 8, 10, 'x', 'x', 'x', 12, 14, 5, 14, 2, 6, 'x', 'x'],
                        ['x', 'x', 'x', 12, 18, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 19, 'x'],
                        [11, 'x', 12, 'x', 'x', 5, 'x', 15, 8, 'x', 9, 'x', 'x', 'x', 'x'],
                        [9, 'x', 4, 'x', 'x', 'x', 'x', 2, 18, 'x', 11, 'x', 11, 'x', 19],
                        [13, 'x', 17, 1, 'x', 14, 'x', 'x', 'x', 'x', 16, 'x', 2, 'x', 'x'],
                        [3, 16, 'x', 'x', 3, 11, 'x', 15, 'x', 'x', 'x', 'x', 'x', 16, 'x']])
   num_rows = 15
   num_cols = 15
   # Define the districts
   districts = [range(0, 4), range(4, 9), range(9, 15)]


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
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current cell to the goal cell
   # The heuristic relaxes the constraint that Ben cannot move through closed workshops and presumes Ben can move to the goal cell in a straight line, thus reporting a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal cell, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal cell from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
