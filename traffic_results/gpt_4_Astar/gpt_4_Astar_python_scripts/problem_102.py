
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the puzzle, represented as 2d tuples
   initial_state = ((5, 0),)
   goal_state = ((7, 13),)
   # Define the map of the city
   city_map = np.array([['x', 13, 'x', 'x', 'x', 'x', 3, 4, 'x', 'x', 9, 'x', 18, 7, 2],
                        [1, 10, 17, 'x', 'x', 'x', 11, 13, 'x', 10, 'x', 9, 13, 'x', 'x'],
                        ['x', 'x', 7, 18, 'x', 'x', 'x', 'x', 7, 'x', 'x', 'x', 1, 'x', 16],
                        [10, 'x', 'x', 'x', 13, 'x', 2, 9, 'x', 'x', 8, 'x', 'x', 5, 'x'],
                        ['x', 7, 12, 'x', 1, 18, 14, 'x', 7, 'x', 'x', 16, 'x', 'x', 19],
                        [5, 1, 13, 17, 11, 14, 16, 'x', 14, 'x', 18, 5, 'x', 18, 'x'],
                        ['x', 15, 19, 4, 'x', 13, 'x', 5, 'x', 'x', 18, 'x', 17, 'x', 'x'],
                        [3, 7, 'x', 'x', 'x', 12, 'x', 'x', 17, 4, 'x', 13, 19, 3, 10],
                        [11, 'x', 'x', 'x', 'x', 2, 2, 19, 13, 4, 7, 17, 16, 'x', 17],
                        [12, 5, 4, 'x', 'x', 'x', 'x', 12, 8, 11, 'x', 17, 14, 19, 2],
                        [4, 10, 'x', 'x', 6, 11, 16, 17, 'x', 'x', 18, 'x', 17, 'x', 'x'],
                        ['x', 'x', 'x', 'x', 11, 9, 18, 17, 12, 'x', 'x', 'x', 'x', 'x', 1],
                        [18, 13, 7, 'x', 'x', 5, 4, 13, 'x', 'x', 19, 12, 1, 18, 'x'],
                        [15, 'x', 17, 'x', 'x', 'x', 17, 'x', 'x', 'x', 10, 'x', 15, 16, 'x'],
                        ['x', 'x', 11, 15, 'x', 'x', 12, 16, 12, 13, 18, 'x', 17, 8, 15]])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [range(0, 6), range(6, 7), range(7, 15)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where the last workshop visited is the destination and at least 1 workshop from each district has been visited
       if state[-1] == goal_state and all(any(workshop[0] in district for workshop in state) for district in districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops from the current workshop
       # Generate the coordinates of the neighboring workshops
       current_workshop = state[-1]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           neighbor_workshop = (current_workshop[0] + d_row, current_workshop[1] + d_col)
           # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city and the workshop is not closed
           if (0 <= neighbor_workshop[0] < num_rows and 0 <= neighbor_workshop[1] < num_cols and
               city_map[neighbor_workshop[0]][neighbor_workshop[1]] != 'x'):
               # The move is valid, generate the new state
               new_state = state + (neighbor_workshop,)
               # The cost so far is the sum of the travel times from the initial workshop to the current workshop
               new_cost = g + int(city_map[neighbor_workshop[0]][neighbor_workshop[1]])


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state, city_map)
                   heapq.heappush(queue, (g + h, new_cost, actions + [neighbor_workshop], new_state))
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic for this problem is the straight-line distance (the shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the straight-line distance, if the workshop is moved toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   h = 0
   current_workshop = state[-1]
   # Calculate the straight-line distance
   h += abs(current_workshop[0] - goal[0]) + abs(current_workshop[1] - goal[1])
   return h


print(a_star())
