
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('e', 'u', 'n', 'a', '_', 'e'),
                   ('d', 'r', 'a', 'v', 'i', 'e'),
                   ('m', 'a', 'n', 'u', 'k', 'a'),
                   ('k', 'h', 'a', 't', 'u', 'm'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'u', 'v', 'a', 't', 'e'),
                 ('d', 'e', 'a', 'r', 'i', 'e'),
                 ('m', 'a', 'n', 'u', 'k', 'a'),
                 ('k', 'h', 'a', 'n', 'u', 'm'))
   num_rows = 4
   num_cols = 6
   # Define the initial position of the blank space
   blank_space = (0, 4)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, blank_space)]


   while queue:
       _, g, actions, state, blank_space = heapq.heappop(queue)


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
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, g + 1, actions + [direction], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile to its goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and that it can only be swapped with a diagonal neighbor
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least the Manhattan distance to reach its goal position
   # It's consistent because moving a tile reduces the Manhattan distance of that tile to its goal position by 1 (if the move is toward the goal), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are at their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = next((x, y) for x, row in enumerate(goal) for y, cell in enumerate(row) if cell == state[i][j])
           h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
