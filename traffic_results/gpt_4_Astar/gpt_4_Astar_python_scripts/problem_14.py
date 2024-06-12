
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 1)
   goal_state = (7, 8)
   # Define the map of the city
   city_map = [['x', 3, 13, 18, 'x', 'x', 3, 'x', 'x'],
               ['x', 3, 'x', 'x', 18, 1, 13, 'x', 'x'],
               ['x', 'x', 'x', 6, 'x', 13, 'x', 11, 1],
               [4, 3, 'x', 'x', 'x', 'x', 6, 6, 11],
               [14, 16, 'x', 'x', 'x', 'x', 'x', 18, 11],
               [14, 'x', 11, 'x', 'x', 4, 'x', 1, 'x'],
               [18, 7, 1, 'x', 8, 'x', 'x', 'x', 'x'],
               [4, 9, 6, 12, 13, 19, 'x', 14, 4],
               ['x', 'x', 17, 12, 7, 7, 9, 3, 1]]
   # Define the districts of the city
   districts = [1, 1, 1, 1, 2, 2, 2, 3, 3]
   # Define the number of rows and columns in the city map
   num_rows = len(city_map)
   num_cols = len(city_map[0])


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[(initial_state, frozenset([districts[initial_state[0]]]))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [initial_state], (initial_state, frozenset([districts[initial_state[0]]])))]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, (state, visited_districts) = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == 3:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               new_visited_districts = visited_districts.union([districts[new_row]])
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + city_map[new_row][new_col]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                   visited_costs[(new_state, new_visited_districts)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], (new_state, new_visited_districts)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
