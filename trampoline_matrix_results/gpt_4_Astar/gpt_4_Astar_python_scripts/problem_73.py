
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the puzzle, represented as 2d tuples
   initial_state = ((1, 12), 0)
   goal_state = (8, 2)
   # Define the map of the park
   park_map = np.array([[1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
                        [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
                        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
                        [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
                        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]])
   num_rows = 13
   num_cols = 13


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state[0] == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the 8 neighboring trampolines
       # Generate the coordinates of the neighboring trampolines
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
           jump_row, jump_col = state[0][0] + d_row, state[0][1] + d_col
           # Check if the jump is valid, ie if the coordinate of the trampoline to be jumped to is a valid coordinate within the bounds of the park and the trampoline is not broken
           if 0 <= jump_row < num_rows and 0 <= jump_col < num_cols and park_map[jump_row][jump_col] == 0:
               # The actions is valid, generate the new state
               new_state = ((jump_row, jump_col), state[1])
               # If the jump is diagonal, increment the count of diagonal jumps by 1
               if abs(d_row) == abs(d_col):
                   new_state = ((jump_row, jump_col), state[1] + 1)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state[0]], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex can only jump to neighboring trampolines and presumes Alex can jump directly to the goal position
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the current position from the goal position would be 0 in the goal state.
   h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
   # If the number of diagonal jumps made is less than 4, add the remaining number of diagonal jumps required to the heuristic
   if state[1] < 4:
       h += 4 - state[1]
   return h


print(a_star())