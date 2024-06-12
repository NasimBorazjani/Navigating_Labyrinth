
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the puzzle, represented as 2d tuples
   initial_state = (11, 9)
   goal_state = (0, 3)
   # Define the map of the park
   park_map = np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                        [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                        [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
                        [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                        [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1]])
   num_rows = 12
   num_cols = 12
   # Define the possible moves from a trampoline
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, 0)]


   while queue:
       _, g, actions, state, num_diagonal_moves = heapq.heappop(queue)


       if state == goal_state:
           return actions


       for move in moves:
           new_state = (state[0] + move[0], state[1] + move[1])
           # Check if the new state is valid, ie within the bounds of the park and the trampoline is not broken
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and park_map[new_state[0]][new_state[1]] == 0):
               # Check if the move is diagonal
               if move[0] != 0 and move[1] != 0:
                   new_num_diagonal_moves = num_diagonal_moves + 1
               else:
                   new_num_diagonal_moves = num_diagonal_moves
               # Check if the number of diagonal moves is valid
               if new_num_diagonal_moves <= 4:
                   new_cost = g + 1
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_moves))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
   # The heuristic relaxes the constraint that Alex can only move to an adjacent trampoline and presumes Alex can move directly to the goal position
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring trampoline is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance from the goal position to itself would be 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
