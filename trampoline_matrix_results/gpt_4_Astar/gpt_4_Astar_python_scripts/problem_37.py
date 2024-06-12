
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (0, 9)
   goal_state = (6, 0)
   # Define the grid of trampolines
   grid = np.array([[1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
                    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                    [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]])
   num_rows = len(grid)
   num_cols = len(grid[0])


   visited_costs = {}
   visited_costs[(initial_state, 0)] = 0


   queue = [(0, 0, [], initial_state, 0)]


   while queue:
       _, g, actions, state, num_diagonal_jumps = heapq.heappop(queue)


       if state == goal_state and num_diagonal_jumps == 3:
           return actions


       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
               new_state = (new_row, new_col)
               new_cost = g + 1
               new_num_diagonal_jumps = num_diagonal_jumps + 1 if d_row != 0 and d_col != 0 else num_diagonal_jumps
               if new_num_diagonal_jumps <= 3 and ((new_state, new_num_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_num_diagonal_jumps)]):
                   visited_costs[(new_state, new_num_diagonal_jumps)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_jumps))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps and presumes Alex can move to the goal position by moving in any direction
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
