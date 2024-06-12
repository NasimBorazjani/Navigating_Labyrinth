
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 0)
   goal_state = (3, 7)
   # Define the map of the city
   city_map = np.array([[8, 'x', 4, 7, 10, 'x', 12, 5, 'x'],
                        ['x', 'x', 4, 11, 16, 4, 12, 15, 'x'],
                        [3, 'x', 16, 16, 4, 'x', 'x', 'x', 'x'],
                        [11, 6, 3, 12, 8, 2, 19, 14, 'x'],
                        [20, 18, 19, 'x', 4, 18, 'x', 15, 13],
                        [8, 15, 'x', 16, 11, 'x', 10, 14, 1],
                        ['x', 'x', 'x', 19, 'x', 'x', 'x', 'x', 'x'],
                        [7, 'x', 'x', 'x', 'x', 'x', 1, 7, 8],
                        [15, 3, 'x', 'x', 'x', 'x', 'x', 'x', 'x']])
   num_rows, num_cols = city_map.shape
   # Define the districts
   districts = [set(range(0, 4)), set(range(4, 5)), set(range(5, 9))]


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
           # Check if the new state would be valid, ie the new workshop must be within the bounds of the city and not be closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + city_map[new_row][new_col]
               # Update the set of visited districts
               new_visited_districts = visited_districts.copy()
               for i, district in enumerate(districts):
                   if new_row in district:
                       new_visited_districts.add(i)


               if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                   visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
