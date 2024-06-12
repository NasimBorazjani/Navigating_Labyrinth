
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the puzzle, represented as 2d tuples
   initial_state = ((4, 0),)
   goal_state = ((9, 11),)
   # Define the map of the city
   city_map = np.array([['x', 2, 16, 'x', 9, 'x', 14, 'x', 8, 'x', 16, 'x', 'x', 4, 8],
                        [9, 'x', 4, 'x', 'x', 7, 11, 'x', 'x', 13, 'x', 'x', 6, 11, 'x'],
                        ['x', 'x', 10, 14, 'x', 'x', 18, 'x', 'x', 'x', 'x', 'x', 6, 16, 'x'],
                        ['x', 14, 'x', 1, 'x', 7, 5, 16, 'x', 19, 'x', 'x', 10, 7, 'x'],
                        [1, 3, 'x', 19, 7, 2, 17, 'x', 'x', 6, 'x', 'x', 'x', 10, 14],
                        [14, 'x', 'x', 'x', 12, 'x', 16, 5, 8, 12, 17, 2, 19, 'x', 5],
                        [9, 9, 8, 15, 18, 'x', 16, 'x', 10, 'x', 'x', 14, 'x', 'x', 'x'],
                        [18, 20, 'x', 'x', 11, 2, 17, 6, 'x', 18, 8, 'x', 6, 16, 'x'],
                        [12, 'x', 'x', 'x', 'x', 7, 14, 4, 8, 12, 3, 'x', 15, 13, 2],
                        [16, 'x', 'x', 'x', 12, 'x', 8, 1, 7, 7, 12, 17, 2, 2, 7],
                        ['x', 13, 3, 3, 1, 'x', 6, 14, 20, 8, 'x', 4, 10, 17, 'x'],
                        [1, 8, 'x', 16, 'x', 'x', 'x', 9, 'x', 'x', 10, 'x', 'x', 5, 8],
                        ['x', 'x', 1, 'x', 'x', 6, 'x', 'x', 'x', 7, 16, 'x', 'x', 'x', 'x'],
                        [14, 'x', 'x', 10, 18, 'x', 6, 13, 'x', 'x', 'x', 'x', 'x', 15, 'x'],
                        ['x', 8, 2, 'x', 17, 'x', 12, 16, 11, 4, 4, 'x', 'x', 17, 'x']])
   num_rows = 15
   num_cols = 15
   # Define the districts
   districts = [range(0, 5), range(5, 10), range(10, 15)]


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
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_workshop = (state[-1][0] + d_row, state[-1][1] + d_col)
           # Check if the move is valid, ie if the coordinate of the new workshop is a valid coordinate within the bounds of the city and the workshop is not closed
           if (0 <= new_workshop[0] < num_rows and 0 <= new_workshop[1] < num_cols and
               city_map[new_workshop[0]][new_workshop[1]] != 'x'):
               # Generate the new state
               new_state = state + (new_workshop,)
               # The cost so far is the sum of the travel times from the initial workshop to the current workshop
               new_cost = g + int(city_map[new_workshop[0]][new_workshop[1]])
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_workshop, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_workshop], new_state))
   return None


def heuristic(workshop, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraint that the car can only move to a neighboring workshop and presumes the car can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
   return abs(workshop[0] - goal[0]) + abs(workshop[1] - goal[1])


print(a_star())
