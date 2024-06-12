
import heapq
import numpy as np


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 'j', '_', 'h', 'u'),
                   ('w', 'l', 'r', 'e', 'y'),
                   ('n', 'i', 'l', 't', 'a'),
                   ('i', 'y', 'i', 'm', 'l'))
   num_rows = 4
   num_cols = 5
   # Define the goal state of the board
   goal_state = (('j', 'e', 'h', 'u', '_'),
                 ('w', 'o', 'r', 'm', 'y'),
                 ('l', 'i', 'n', 't', 'y'),
                 ('i', 'l', 'i', 'a', 'l'))
   # Define the initial position of the blank space
   blank_space = (0, 2)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, blank_space)]


   while queue:
       _, g, actions, state, blank_space = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col, direction in [(1, 1, 'down-right'), (-1, -1, 'up-left'), (-1, 1, 'up-right'), (1, -1, 'down-left')]:
           new_row, new_col = blank_space[0] + d_row, blank_space[1] + d_col
           # Check if the new position of the blank space is valid, ie if it is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_space[0]][blank_space[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space[0]][blank_space[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in the current state to its position in the goal state
   # The heuristic relaxes the constraint that only the blank space can be moved, and only to a position occupied by one of its 4 diagonal neighbors
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving the blank space to an adjacent position is 1, which is always greater than or equal to the decrease in the Manhattan distance of the tile that was swapped with the blank space
   # Also the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = np.where(np.array(goal) == state[i][j])
           h += abs(i - goal_i[0]) + abs(j - goal_j[0])
   return h


print(a_star())
