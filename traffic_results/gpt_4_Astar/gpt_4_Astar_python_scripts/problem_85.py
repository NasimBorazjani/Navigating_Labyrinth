
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (10, 12)
   goal_state = (4, 3)
   # Define the map of the city
   city_map = np.array([[5, 10, 'x', 'x', 'x', 16, 'x', 'x', 'x', 16, 'x', 10, 8, 'x'],
                        [1, 'x', 13, 'x', 7, 'x', 'x', 'x', 10, 3, 3, 13, 18, 11],
                        [14, 'x', 'x', 'x', 9, 16, 16, 15, 'x', 'x', 15, 'x', 4, 4],
                        [15, 'x', 3, 'x', 'x', 17, 'x', 16, 10, 9, 'x', 6, 16, 17],
                        [12, 8, 'x', 10, 'x', 'x', 13, 10, 'x', 'x', 6, 3, 'x', 1],
                        ['x', 'x', 'x', 5, 8, 9, 6, 14, 1, 'x', 'x', 2, 12, 'x'],
                        [13, 'x', 'x', 'x', 16, 6, 'x', 17, 12, 18, 'x', 17, 8, 'x'],
                        [10, 'x', 14, 15, 'x', 'x', 'x', 20, 'x', 17, 18, 8, 'x', 4],
                        ['x', 11, 3, 'x', 'x', 'x', 'x', 7, 'x', 4, 'x', 'x', 11, 2],
                        [7, 'x', 'x', 10, 'x', 19, 'x', 7, 17, 'x', 'x', 14, 'x', 15],
                        [12, 11, 'x', 'x', 9, 7, 'x', 15, 1, 5, 5, 11, 15, 'x'],
                        ['x', 9, 9, 'x', 'x', 'x', 'x', 8, 'x', 8, 19, 11, 12, 12],
                        ['x', 17, 5, 'x', 'x', 17, 'x', 'x', 12, 'x', 15, 12, 10, 'x'],
                        [18, 'x', 'x', 'x', 3, 'x', 7, 'x', 8, 5, 12, 8, 10, 'x']])
   num_rows, num_cols = city_map.shape
   # Define the districts
   districts = [range(0, 5), range(5, 10), range(10, 14)]


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


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben cannot move through closed workshops and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
