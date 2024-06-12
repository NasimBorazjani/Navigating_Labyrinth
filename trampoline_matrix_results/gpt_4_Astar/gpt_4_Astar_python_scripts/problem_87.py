
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as 2d tuples
   initial_state = ((0, 11), 0)
   goal_state = (12, 2)
   # Define the map of the trampoline park
   park_map = np.array([[1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
                        [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                        [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                        [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
                        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]])
   num_rows = 14
   num_cols = 14


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state[0] == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_row, new_col = state[0][0] + d_row, state[0][1] + d_col
           # Check if the new state would be valid, ie the new position must be within the bounds of the park and the trampoline at the new position must not be broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # Generate the new state
               new_state = ((new_row, new_col), state[1] + int(abs(d_row) == abs(d_col)))
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the 8 adjacent trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   return abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])


print(a_star())
