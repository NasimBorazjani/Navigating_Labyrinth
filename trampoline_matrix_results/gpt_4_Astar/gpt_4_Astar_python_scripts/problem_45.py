
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (1, 0)
   goal_state = (8, 9)
   # Define the map of the park
   park_map = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
                        [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
                        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                        [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]])
   num_rows = len(park_map)
   num_cols = len(park_map[0])
   # Define the directions of the 8 possible jumps
   directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


   visited_costs = {}
   visited_costs[(initial_state, 0)] = 0


   queue = [(0, 0, [], initial_state, 0)]


   while queue:
       _, g, actions, state, num_diagonal_jumps = heapq.heappop(queue)


       if state == goal_state and num_diagonal_jumps == 3:
           return actions


       for direction in directions:
           new_state = (state[0] + direction[0], state[1] + direction[1])
           # Check if the new state is valid, ie within the bounds of the park and the trampoline is not broken
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and park_map[new_state[0]][new_state[1]] == 0):
               # Check if the jump is diagonal
               if direction in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                   new_num_diagonal_jumps = num_diagonal_jumps + 1
               else:
                   new_num_diagonal_jumps = num_diagonal_jumps
               # Check if the new state is valid, ie the number of diagonal jumps is less than or equal to 3
               if new_num_diagonal_jumps <= 3:
                   new_cost = g + 1
                   if (new_state, new_num_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_num_diagonal_jumps)]:
                       visited_costs[(new_state, new_num_diagonal_jumps)] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_jumps))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps and presumes Alex can move to the goal state by jumping to any of the 8 neighboring trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring trampoline is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
