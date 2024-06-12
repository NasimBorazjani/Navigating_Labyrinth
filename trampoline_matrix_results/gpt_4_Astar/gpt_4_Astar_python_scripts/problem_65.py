
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = ((0, 0), 0)
   goal_state = (8, 9)
   # Define the grid of the trampoline park
   grid = np.array([[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
                    [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                    [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                    [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
   num_rows = len(grid)
   num_cols = len(grid[0])


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
           # Check if the new state would be valid, ie the new position must be within the bounds of the grid and the trampoline at the new position must not be broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
               # Generate the new state
               new_state = ((new_row, new_col), state[1] + int(d_row != 0 and d_col != 0))
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance from the current position to the goal position, as the shortest path to the goal position is the Manhattan distance, if there are no broken trampolines in the way
                   h = abs(new_row - goal_state[0]) + abs(new_col - goal_state[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
   return None


print(a_star())
