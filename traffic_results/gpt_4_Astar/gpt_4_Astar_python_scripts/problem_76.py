
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (4, 3)
   goal_state = (8, 13)
   # Define the districts in the city
   districts = [(0, 2), (3, 7), (8, 13)]
   # Define the map of the city
   city_map = np.array([['x', 12, 8, 4, 4, 16, 8, 'x', 'x', 17, 18, 9, 'x', 16],
                        [2, 9, 'x', 1, 4, 13, 20, 11, 2, 'x', 11, 7, 14, 12],
                        ['x', 'x', 'x', 'x', 17, 15, 8, 12, 'x', 'x', 7, 'x', 'x', 'x'],
                        [2, 2, 'x', 5, 14, 'x', 1, 5, 4, 14, 7, 'x', 'x', 'x'],
                        [19, 'x', 11, 1, 19, 19, 12, 'x', 12, 13, 5, 3, 17, 17],
                        ['x', 'x', 'x', 'x', 'x', 1, 'x', 'x', 4, 'x', 'x', 'x', 8, 19],
                        [6, 'x', 10, 'x', 7, 1, 11, 'x', 'x', 3, 'x', 3, 2, 'x'],
                        [19, 'x', 3, 11, 'x', 6, 11, 'x', 12, 14, 10, 'x', 11, 18],
                        [13, 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 'x', 'x', 10, 5],
                        [19, 'x', 'x', 16, 'x', 'x', 18, 'x', 8, 'x', 2, 11, 'x', 12],
                        ['x', 14, 'x', 6, 'x', 18, 'x', 11, 'x', 'x', 14, 11, 2, 'x'],
                        ['x', 'x', 6, 8, 10, 8, 14, 'x', 'x', 13, 'x', 10, 'x', 19],
                        ['x', 19, 'x', 7, 12, 17, 'x', 15, 'x', 16, 19, 'x', 5, 'x'],
                        [8, 'x', 17, 'x', 'x', 5, 15, 'x', 'x', 16, 1, 'x', 'x', 17]], dtype=object)
   num_rows, num_cols = city_map.shape


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, [False]*len(districts))]


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
               new_cost = g + city_map[new_row][new_col]
               # Check if the new state is in a new district
               new_visited_districts = visited_districts[:]
               for i, (start, end) in enumerate(districts):
                   if start <= new_row <= end:
                       new_visited_districts[i] = True
                       break


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben cannot move through closed workshops and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
