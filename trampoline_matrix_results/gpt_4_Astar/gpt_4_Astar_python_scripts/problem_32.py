
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (0, 9)
   goal_state = (9, 2)
   # Define the map of the park
   park_map = np.array([[1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]])
   num_rows = park_map.shape[0]
   num_cols = park_map.shape[1]
   # Define the number of diagonal jumps Alex must make
   num_diagonal_jumps = 3


   visited_costs = {}
   visited_costs[(initial_state, num_diagonal_jumps)] = 0


   queue = [(0, 0, [], initial_state, num_diagonal_jumps)]


   while queue:
       _, g, actions, state, num_diagonal_jumps_left = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and num_diagonal_jumps_left == 0:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 neighboring trampolines
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position must be within the bounds of the park and the trampoline at the new position must not be broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
               # If the jump was diagonal, decrement the number of diagonal jumps left
               new_num_diagonal_jumps_left = num_diagonal_jumps_left - 1 if abs(d_row) == abs(d_col) else num_diagonal_jumps_left
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if (new_state, new_num_diagonal_jumps_left) not in visited_costs or new_cost < visited_costs[(new_state, new_num_diagonal_jumps_left)]:
                   visited_costs[(new_state, new_num_diagonal_jumps_left)] = new_cost
                   h = heuristic(new_state, goal_state, new_num_diagonal_jumps_left)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_jumps_left))
   return None


def heuristic(state, goal, num_diagonal_jumps_left):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
   # The heuristic relaxes the constraint that Alex can only jump to neighboring trampolines and presumes Alex can jump directly to the goal position
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal position to itself is 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # If Alex has not made all the required diagonal jumps, he must make at least one more jump, thus increment the heuristic by 1
   if num_diagonal_jumps_left > 0:
       h += 1
   return h


print(a_star())
