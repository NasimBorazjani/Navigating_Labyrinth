
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as 2d tuples
   initial_state = ((2, 13),)
   goal_state = ((5, 1),)
   # Define the map of the city
   city_map = np.array([['x', 'x', '14', 'x', '3', 'x', '18', 'x', '4', '4', 'x', 'x', '16', 'x'],
                        ['x', 'x', '1', '15', 'x', '18', 'x', '18', 'x', 'x', 'x', 'x', '14', 'x'],
                        ['x', 'x', '7', '14', 'x', 'x', '16', 'x', 'x', 'x', 'x', '5', '19', '15'],
                        ['x', '13', '18', 'x', '17', 'x', '6', '8', 'x', '8', 'x', 'x', '13', 'x'],
                        ['12', 'x', '15', 'x', 'x', 'x', 'x', '18', 'x', 'x', 'x', '8', '6', '7'],
                        ['5', '11', '14', '14', '11', '5', '13', '7', 'x', 'x', '10', '12', '17', '17'],
                        ['14', 'x', '3', '15', '3', 'x', 'x', '17', '12', '7', '19', '15', '4', '5'],
                        ['x', '2', '14', 'x', '8', 'x', '9', '19', '16', '14', '17', '12', 'x', '13'],
                        ['x', 'x', '2', '15', 'x', 'x', 'x', '2', '14', '17', '3', '4', 'x', '12'],
                        ['2', 'x', '11', 'x', 'x', '14', 'x', 'x', '16', 'x', '11', '13', 'x', 'x'],
                        ['17', 'x', 'x', '2', '9', '14', '8', 'x', '11', '5', 'x', '10', '5', 'x'],
                        ['4', 'x', '8', '8', '11', 'x', '16', 'x', 'x', 'x', '15', 'x', '2', '16'],
                        ['x', '16', 'x', 'x', '9', 'x', 'x', 'x', 'x', '19', '6', '9', 'x', 'x'],
                        ['x', '14', '9', 'x', '6', '1', '7', 'x', '10', '4', 'x', 'x', 'x', 'x']])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts of the city
   districts = [range(0, 3), range(3, 6), range(6, 14)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where Ben has visited at least 1 workshop in each district and has reached the destination workshop
       if (state[-1] == goal_state and
           all(any(workshop[0] in district for workshop in state) for district in districts)):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops from the current workshop
       # Generate the coordinates of the neighboring workshops
       current_workshop = state[-1]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           neighbor_workshop = (current_workshop[0] + d_row, current_workshop[1] + d_col)
           # Check if the move is valid, ie if the coordinate of the neighboring workshop is a valid coordinate within the bounds of the city and the workshop is not closed
           if (0 <= neighbor_workshop[0] < num_rows and
               0 <= neighbor_workshop[1] < num_cols and
               city_map[neighbor_workshop] != 'x'):
               # The action is valid, generate the new state
               new_state = state + (neighbor_workshop,)
               # The cost so far is the sum of the travel times from the initial workshop to the current workshop
               new_cost = g + int(city_map[neighbor_workshop])


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state, city_map)
                   heapq.heappush(queue, (g + h, new_cost, actions + [neighbor_workshop], new_state))
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic for this problem is the straight-line distance (the shortest path) from the current workshop to the goal workshop, multiplied by the minimum travel time between any two workshops in the city
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop from the current workshop
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to the decrease in the straight-line distance, if the workshop is moved toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   min_travel_time = min(int(cell) for row in city_map for cell in row if cell != 'x')
   h = min_travel_time * ((goal[0] - state[-1][0]) ** 2 + (goal[1] - state[-1][1]) ** 2) ** 0.5
   return h


print(a_star())
