
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 7)
   goal_state = (7, 0)
   # Define the map of the city
   city_map = np.array([[10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x', 'x'],
                        [2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5],
                        ['x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13],
                        [1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10],
                        [9, 'x', 17, 'x', 'x', 7, 'x', 'x', 1, 'x', 14],
                        [16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'],
                        [9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14],
                        [2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6],
                        [3, 'x', 18, 6, 'x', 14, 'x', 'x', 'x', 8, 19],
                        [2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'],
                        ['x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5]])
   num_rows, num_cols = city_map.shape
   # Define the districts of the city
   districts = [range(0, 3), range(3, 7), range(7, 11)]
   # Define the directions in which Ben can move
   directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == len(districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for direction in directions:
           new_state = (state[0] + direction[0], state[1] + direction[1])
           # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state] != 'x'):
               # The cost so far is the travel time from the current workshop to the new workshop
               new_cost = g + city_map[new_state]
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
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current workshop to the goal workshop
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is the shortest path in a grid where you can only move in 4 directions
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward the goal workshop
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # Add a large penalty if all districts have not been visited yet
   if len(visited_districts) < len(districts):
       h += 1000
   return h


print(a_star())
