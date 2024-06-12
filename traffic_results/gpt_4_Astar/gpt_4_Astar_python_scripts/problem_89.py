
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as 2d tuples
   initial_state = ((3, 13),)
   goal_state = ((4, 0),)
   # Define the map of the city
   city_map = np.array([['x', 'x', 'x', '7', '11', '16', '13', '19', '15', 'x', '19', 'x', 'x', '16'],
                        ['9', 'x', '14', 'x', '7', '3', 'x', 'x', '17', '9', 'x', 'x', 'x', '19'],
                        ['x', '11', '6', '18', 'x', '19', '4', 'x', 'x', 'x', '19', '12', '4', '17'],
                        ['5', '12', '15', '3', 'x', 'x', 'x', 'x', '7', 'x', '11', '17', '20', '20'],
                        ['6', 'x', '11', '15', '11', '17', '16', '5', 'x', '3', '4', '20', 'x', '14'],
                        ['x', '11', 'x', '6', 'x', '16', '2', '18', '5', '11', 'x', '14', '4', '7'],
                        ['x', '6', 'x', '17', 'x', 'x', '15', '7', 'x', '2', '3', '16', '7', '15'],
                        ['7', 'x', 'x', '8', '1', 'x', 'x', 'x', '14', 'x', 'x', '18', 'x', '19'],
                        ['13', 'x', 'x', 'x', 'x', '2', '9', '19', 'x', '16', '11', '5', 'x', '11'],
                        ['x', '17', '15', '18', 'x', '7', 'x', '15', '13', 'x', '14', '2', 'x', '19'],
                        ['x', 'x', 'x', '14', '7', '19', 'x', 'x', '9', '9', 'x', 'x', 'x', 'x'],
                        ['x', '3', '13', '15', '18', '17', 'x', 'x', '9', '4', 'x', '12', '10', '14'],
                        ['15', 'x', '6', '19', '19', '19', 'x', '1', '8', '4', '17', '14', 'x', 'x'],
                        ['8', 'x', '14', '7', '12', '6', '8', 'x', '5', 'x', '11', '11', 'x', 'x']])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [range(0, 4), range(4, 6), range(6, 14)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where Ben has visited at least 1 workshop in each district and reached the destination workshop
       if (state[-1] == goal_state and
           all(any(workshop[0] in district for workshop in state) for district in districts)):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops from the current workshop
       # Generate the coordinates of the neighboring workshops
       current_workshop = state[-1]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           neighbor_workshop = (current_workshop[0] + d_row, current_workshop[1] + d_col)
           # Check if the move is valid, ie if the coordinate of the neighboring workshop is a valid coordinate within the bounds of the city map and the workshop is not closed
           if (0 <= neighbor_workshop[0] < num_rows and
               0 <= neighbor_workshop[1] < num_cols and
               city_map[neighbor_workshop] != 'x'):
               # The move is valid, generate the new state
               new_state = state + (neighbor_workshop,)
               # The cost so far is the sum of the travel times from the initial workshop to the current workshop, as the task is to minimize the total travel time
               new_cost = g + int(city_map[neighbor_workshop])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(neighbor_workshop, goal_state, city_map), new_cost, actions + [neighbor_workshop], new_state))
   return None


def heuristic(workshop, goal, city_map):
   # An admissible and consistent heuristic is the straight-line distance (the shortest path) from the current workshop to the goal workshop, multiplied by the minimum travel time between any two workshops in the city
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes he can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the decrease in the straight-line distance, if the workshop is moved toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal workshop is 0, as the distance of the goal workshop from itself would be 0.
   h = (abs(workshop[0] - goal[0]) + abs(workshop[1] - goal[1])) * int(np.min(city_map[city_map != 'x']))
   return h


print(a_star())
