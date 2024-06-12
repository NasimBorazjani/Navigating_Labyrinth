
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('p', 'j', 'm', 'y'),
                   ('e', 'h', 'p', 'o'),
                   ('y', 'o', '_', 'e'),
                   ('r', 'a', 'o', 'n'),
                   ('w', 'a', 'r', 'd'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'j', 'a', 'y'),
                 ('e', 'p', 'p', 'y'),
                 ('h', 'o', 'm', 'e'),
                 ('r', 'o', 'o', 'n'),
                 ('w', 'a', 'r', 'd'))
   num_rows = 5
   num_cols = 4
   # Define the possible actions as a dictionary, with the keys being the action names and the values being the change in the row and column indices of the blank space
   actions = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, path, state = heapq.heappop(queue)


       if state == goal_state:
           return path


       # Get the coordinates of the blank space in the current state
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for action, (d_row, d_col) in actions.items():
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, path + [action], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and that it can only be swapped with one of its 4 diagonal neighbors
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving a tile from one position to another reduces the Manhattan distance of the tile by a max of 1 (if the moved tile's goal position is a diagonal neighbor), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(x, y) for x, row in enumerate(goal) for y, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
