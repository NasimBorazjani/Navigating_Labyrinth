
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('h', 'n', '_', 'd'),
                   ('w', 'r', 'a', 'e'),
                   ('e', 'o', 'y', 't'),
                   ('h', 'e', 'l', 'm'),
                   ('m', 'i', 'l', 'k'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'n', 'e', 'd'),
                 ('w', 'h', 'a', 'm'),
                 ('r', 'o', 'y', 't'),
                 ('h', 'e', 'l', 'l'),
                 ('m', 'i', 'e', 'k'))
   num_rows = 5
   num_cols = 4
   # Define the initial position of the blank space
   blank_space = (0, 2)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, blank_space)]


   while queue:
       _, g, actions, state, blank_space = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
           new_row, new_col = blank_space[0] + d_row, blank_space[1] + d_col
           # Check if the new position of the blank space is valid, ie if it is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_space[0]][blank_space[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space[0]][blank_space[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [direction], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a position occupied by one of its 4 diagonal neighbors
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving a tile from one position to another reduces the Manhattan distance of the tile by a max of 1 (if the moved tile's goal position is a diagonal neighbor), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = next((x, y) for x, row in enumerate(goal) for y, cell in enumerate(row) if cell == state[i][j])
           h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
