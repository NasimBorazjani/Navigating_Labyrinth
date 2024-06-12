
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (12, 0)
   goal_state = (3, 8)
   # Define the map of the trampoline park
   park_map = np.array([[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
                        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
                        [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]])
   num_rows = len(park_map)
   num_cols = len(park_map[0])
   # Define the number of diagonal jumps Alex must make
   num_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[(initial_state, num_diagonal_jumps)] = 0


   queue = [(0, 0, [], initial_state, num_diagonal_jumps)]


   while queue:
       _, g, actions, state, num_diagonal_jumps = heapq.heappop(queue)


       if state == goal_state and num_diagonal_jumps == 0:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position must be within the bounds of the park and the trampoline at the new position must not be broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
               # If the jump was diagonal, decrement the number of diagonal jumps remaining
               new_num_diagonal_jumps = num_diagonal_jumps - 1 if abs(d_row) == abs(d_col) else num_diagonal_jumps
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if (new_state, new_num_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_num_diagonal_jumps)]:
                   visited_costs[(new_state, new_num_diagonal_jumps)] = new_cost
                   h = heuristic(new_state, goal_state, new_num_diagonal_jumps)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_jumps))
   return None


def heuristic(state, goal, num_diagonal_jumps):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the 8 adjacent trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # If there are remaining diagonal jumps, add the number of remaining diagonal jumps to the heuristic, as each diagonal jump would require at least 1 action
   if num_diagonal_jumps > 0:
       h += num_diagonal_jumps
   return h


print(a_star())
