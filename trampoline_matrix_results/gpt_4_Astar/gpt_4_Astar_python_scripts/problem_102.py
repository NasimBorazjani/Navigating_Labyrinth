
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as 2d tuples
   initial_state = ((14, 13), 0)
   goal_state = (2, 5)
   # Define the map of the trampoline park
   park_map = np.array([[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
                        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
                        [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
                        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
                        [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]])
   num_rows = 15
   num_cols = 15
   num_diagonal_jumps = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state[0] == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the 8 neighboring trampolines
       # Generate the coordinates of the neighboring trampolines
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
           new_row, new_col = state[0][0] + d_row, state[0][1] + d_col
           # Check if the jump is valid, ie if the coordinate of the trampoline to jump to is a valid coordinate within the bounds of the park and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # The action is valid, generate the new state
               new_state = ((new_row, new_col), state[1])
               # If the jump is diagonal, increment the count of diagonal jumps
               if abs(d_row) == abs(d_col):
                   new_state = ((new_row, new_col), state[1] + 1)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, num_diagonal_jumps), new_cost, actions + [new_state[0]], new_state))
   return None


def heuristic(state, goal, num_diagonal_jumps):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 5 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the neighboring trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
   # If the number of diagonal jumps made is less than 5, add the difference to the heuristic, as Alex must make at least that many more jumps to reach the goal state
   if state[1] < num_diagonal_jumps:
       h += num_diagonal_jumps - state[1]
   return h


print(a_star())
