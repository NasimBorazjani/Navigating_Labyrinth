
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the puzzle, represented as 2d tuples
   initial_state = ((12, 0), 0)
   goal_state = (1, 6)
   # Define the map of the trampoline park
   park_map = np.array([[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
                        [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
                        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]])
   num_rows = 13
   num_cols = 13


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [initial_state[0]], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state[0] == goal_state:
           return actions


       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = state[0][0] + d_row, state[0][1] + d_col
           # Check if the new state is valid, ie if the coordinate of the new state is a valid coordinate within the bounds of the park and the trampoline at the new state is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # The new state is valid, generate the new state
               new_state = ((new_row, new_col), state[1] + int(abs(d_row) == abs(d_col)))
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state[0]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the neighboring trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the current position from the goal position would be 0 in the goal state.
   h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
   return h


print(a_star())
