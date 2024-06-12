
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('l', 'g', 'a', 'n', 'g'),
                   ('c', 'o', 'o', 'e', 'n'),
                   ('e', 'r', '_', 'n', 't'),
                   ('d', 'b', 'w', 'o', 'x'),
                   ('t', 'h', 'w', 'r', 'p'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('g', 'o', 'n', 'g', '_'),
                ('c', 'l', 'o', 'w', 'n'),
                ('b', 'r', 'e', 'n', 't'),
                ('d', 'e', 'w', 'a', 'x'),
                ('t', 'h', 'o', 'r', 'p'))
   num_rows = 5
   num_cols = 5
   # Define the possible moves for the blank space
   moves = [(1, -1), (-1, 1), (1, 1), (-1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Get the coordinates of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       # Generate all possible actions from the current state, which includes moving the blank space to any of its 4 diagonal neighbors
       for d_row, d_col in moves:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The action taken is the direction in which the blank space was moved
                   action = ''
                   if d_row == -1 and d_col == 1:
                       action = 'up-right'
                   elif d_row == 1 and d_col == -1:
                       action = 'down-left'
                   elif d_row == -1 and d_col == -1:
                       action = 'up-left'
                   elif d_row == 1 and d_col == 1:
                       action = 'down-right'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [action], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a position occupied by one of its 4 diagonal neighbors
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving the blank space to a position occupied by a tile reduces the Manhattan distance of that tile to its goal position by a max of 1 (if the tile is moved closer to its goal position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
