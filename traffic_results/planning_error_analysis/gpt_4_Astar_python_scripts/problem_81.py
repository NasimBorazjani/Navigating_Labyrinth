
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (2, 0)
   goal_state = (6, 11)
   num_rows = 14
   num_cols = 14
   # Define the districts
   districts = [(0, 2), (3, 5), (6, 13)]
   # Define the map of the city
   city_map = np.array([[8, 15, 3, 10, 6, 15, 'x', 4, 'x', 'x', 'x', 'x', 'x', 4],
                        [3, 'x', 14, 8, 16, 19, 'x', 18, 4, 'x', 2, 'x', 6, 'x'],
                        [18, 18, 'x', 4, 'x', 17, 11, 10, 17, 9, 'x', 4, 1, 5],
                        ['x', 2, 'x', 12, 1, 'x', 13, 17, 14, 15, 17, 'x', 15, 'x'],
                        ['x', 'x', 'x', 15, 'x', 2, 2, 11, 7, 'x', 5, 7, 4, 18],
                        [16, 'x', 5, 'x', 19, 12, 5, 9, 13, 16, 9, 'x', 3, 'x'],
                        ['x', 'x', 'x', 'x', 14, 18, 'x', 16, 13, 'x', 1, 5, 10, 'x'],
                        [3, 11, 'x', 1, 8, 'x', 'x', 'x', 18, 8, 11, 'x', 'x', 6],
                        [19, 2, 'x', 19, 5, 'x', 'x', 'x', 9, 'x', 6, 'x', 'x', 4],
                        ['x', 2, 'x', 10, 9, 15, 'x', 'x', 'x', 16, 'x', 8, 'x', 'x'],
                        [18, 8, 10, 'x', 3, 'x', 11, 'x', 17, 'x', 17, 'x', 'x', 'x'],
                        [14, 12, 'x', 2, 'x', 19, 2, 19, 14, 'x', 'x', 'x', 3, 'x'],
                        [7, 'x', 'x', 'x', 'x', 'x', 'x', 9, 8, 7, 'x', 15, 2, 'x'],
                        ['x', 'x', 15, 'x', 'x', 15, 16, 'x', 'x', 'x', 19, 'x', 13, 1]])

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, [False]*len(districts))]

   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, visited_districts = heapq.heappop(queue)

       # Check if the current state is the goal state
       if state == goal_state and all(visited_districts):
           return actions

       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the travel time to the new workshop
               new_cost = g + int(city_map[new_row][new_col])
               # Check if the new workshop is in a new district
               new_visited_districts = visited_districts[:]
               for i, (start, end) in enumerate(districts):
                   if start <= new_row <= end:
                       new_visited_districts[i] = True
                       break

               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move to the goal workshop in a straight line
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor workshop is the same or higher, and the heuristic estimate for the goal workshop is 0, as the distance of the goal workshop from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
