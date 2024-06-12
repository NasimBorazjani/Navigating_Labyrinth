
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 3)
   goal_state = (8, 11)
   num_rows = 12
   num_cols = 12
   # Define the districts in the city
   districts = [(0, 2), (3, 7), (8, 11)]
   # Define the map of the city
   city_map = np.array([[10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                        [11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'],
                        ['x', 5, 'x', 'x', 10, 13, 13, 19, 10, 'x', 1, 12],
                        [6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'],
                        [4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6],
                        ['x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'],
                        [19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11],
                        ['x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11],
                        ['x', 4, 'x', 8, 'x', 11, 'x', 'x', 9, 'x', 'x', 15],
                        [10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17],
                        [19, 'x', 3, 11, 'x', 'x', 9, 3, 15, 'x', 5, 17],
                        [18, 'x', 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8]])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, [False]*len(districts))]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and all(visited_districts):
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
               # Check if the new workshop is in a new district
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
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraint that the car can only move to a neighboring workshop and presumes the car can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
