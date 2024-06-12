
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 12)
   goal_state = (1, 2)
   # Define the districts in the city
   districts = [(0, 1), (2, 5), (6, 12)]
   # Define the map of the city
   city_map = np.array([[18, 'x', 'x', 'x', 19, 'x', 'x', 8, 6, 3, 'x', 'x', 'x'],
                        ['x', 'x', 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 4, 6, 4],
                        [1, 4, 15, 13, 17, 11, 'x', 15, 'x', 13, 1, 'x', 'x'],
                        [3, 'x', 6, 1, 15, 2, 'x', 13, 13, 'x', 10, 'x', 'x'],
                        [17, 12, 13, 11, 6, 1, 3, 'x', 'x', 19, 6, 6, 'x'],
                        ['x', 17, 7, 12, 1, 15, 17, 20, 3, 'x', 'x', 18, 10],
                        [16, 14, 15, 'x', 'x', 11, 'x', 17, 20, 15, 7, 10, 'x'],
                        [5, 11, 'x', 7, 19, 'x', 6, 18, 15, 'x', 8, 'x', 1],
                        [10, 'x', 1, 'x', 'x', 6, 'x', 11, 'x', 13, 'x', 'x', 'x'],
                        ['x', 'x', 'x', 'x', 4, 'x', 8, 'x', 12, 'x', 12, 13, 'x'],
                        ['x', 'x', 18, 14, 'x', 'x', 5, 'x', 'x', 13, 1, 'x', 'x'],
                        ['x', 'x', 1, 17, 8, 18, 'x', 7, 'x', 'x', 16, 8, 'x'],
                        ['x', 'x', 'x', 16, 1, 'x', 19, 'x', 'x', 'x', 'x', 14, 'x']])
   num_rows, num_cols = city_map.shape


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
               # Check if the new state is in a new district
               new_visited_districts = set(visited_districts)
               for i, district in enumerate(districts):
                   if district[0] <= new_row <= district[1] and i not in visited_districts:
                       new_visited_districts.add(i)
               new_visited_districts = frozenset(new_visited_districts)


               if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                   visited_costs[(new_state, new_visited_districts)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben can't move through closed workshops and presumes he can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
