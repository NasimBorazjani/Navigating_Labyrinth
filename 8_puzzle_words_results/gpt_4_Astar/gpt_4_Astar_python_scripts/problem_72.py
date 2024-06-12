
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 'l', '_', 't'),
                   ('p', 'r', 'o', 'a'),
                   ('e', 'i', 'k', 'k'),
                   ('c', 'i', 'k', 'a'),
                   ('s', 'l', 'r', 'm'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'l', 'i', 't'),
                 ('p', 'o', 'o', 'r'),
                 ('k', 'i', 'r', 'k'),
                 ('c', 'a', 'k', 'e'),
                 ('s', 'l', 'a', 'm'))
   num_rows = 5
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       # First, find the coordinates of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col, direction in [(1, 1, 'up-right'), (-1, -1, 'down-left'), (-1, 1, 'up-left'), (1, -1, 'down-right')]:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile to its goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a diagonal position
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once
   # It's consistent because moving a tile from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved tile's goal position is a diagonal neighbor), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(x, y) for x, row in enumerate(goal) for y, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
