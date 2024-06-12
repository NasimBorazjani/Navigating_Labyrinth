
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('y', 'c', 'a', 'r', 'd'),
                   ('s', 'u', 'l', 'c', 'a'),
                   ('v', 'h', '_', 'n', 'o'),
                   ('s', 'e', 'l', 's', 'm'),
                   ('b', 'i', 'u', 'h', 'y'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('c', 'a', 'r', 'd', '_'),
                ('s', 'y', 'l', 'v', 'a'),
                ('s', 'h', 'u', 'n', 'e'),
                ('s', 'o', 'l', 'u', 'm'),
                ('b', 'i', 'c', 'h', 'y'))
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
       # Generate all possible actions from the current state, which includes moving the blank space to any of the 4 diagonal directions
       for d_row, d_col in moves:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the blank space can be moved to the new position
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
                   # The action is represented as a tuple of the direction of the move and the character that was swapped with the blank space
                   action = (direction((blank_coord[0], blank_coord[1]), (new_row, new_col)), new_state[blank_coord[0]][blank_coord[1]])
                   heapq.heappush(queue, (g + h, new_cost, actions + [action], new_state))
   return None


def heuristic(state, goal):
   # The heuristic function is the sum of the Manhattan distances from each tile to its goal position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


def direction(coord1, coord2):
   # The direction of the move is determined by the change in the row and column indices
   d_row = coord2[0] - coord1[0]
   d_col = coord2[1] - coord1[1]
   if d_row == 1 and d_col == -1:
       return 'up-right'
   elif d_row == -1 and d_col == 1:
       return 'down-left'
   elif d_row == 1 and d_col == 1:
       return 'down-right'
   elif d_row == -1 and d_col == -1:
       return 'up-left'


print(a_star())
