
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('v', 't', 'u', 'i'),
                   ('o', 'w', 'e', 'i'),
                   ('y', 'd', '_', 'c'),
                   ('d', 'i', 'e', 'm'))
   num_rows = 4
   num_cols = 4
   target_words = ['twi', 'ovey', 'udic', 'diem']
   # The goal state is the target words with the blank space in the top left corner
   goal_state = (('_', 't', 'w', 'i'),
                 ('o', 'v', 'e', 'y'),
                 ('u', 'd', 'i', 'c'),
                 ('d', 'i', 'e', 'm'))
   # The blank space can be swapped with any of its 4 diagonal neighbors
   moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Get the coordinates of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in moves:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The direction of the move is the opposite of the direction of the swap, as the blank space is moved
                   move_direction = moves[moves.index((d_row, d_col))][::-1]
                   # Convert the direction to the required format
                   if move_direction == (1, 1):
                       move = 'up-right'
                   elif move_direction == (1, -1):
                       move = 'up-left'
                   elif move_direction == (-1, 1):
                       move = 'down-right'
                   elif move_direction == (-1, -1):
                       move = 'down-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [move], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # The heuristic relaxes the constraints that only the blank space can be moved and that it can only be swapped with its 4 diagonal neighbors; ie It presumes we can move any tile to any position in the board
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving the blank space to an adjacent position is 1, which is always greater than or equal to the decrease in the Manhattan distance of the tile swapped with the blank space
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
