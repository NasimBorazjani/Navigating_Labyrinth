
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 't', 'f', 'a', 'g'),
                   ('h', 'r', 'p', 'r', 'd'),
                   ('s', 'h', '_', 'l', 't'),
                   ('n', 'e', 'a', 'e', 'h'),
                   ('f', 'a', 'e', 's', 'e'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('t', 'r', 'a', 'g', '_'),
                ('h', 'o', 'p', 'e', 'd'),
                ('s', 'h', 'e', 'l', 'f'),
                ('n', 'e', 'a', 't', 'h'),
                ('f', 'a', 'r', 's', 'e'))
   num_rows = 5
   num_cols = 5
   # Define the possible moves for the blank space
   moves = [('up-right', (-1, 1)), ('down-right', (1, 1)), ('up-left', (-1, -1)), ('down-left', (1, -1))]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the blank space to any of its 4 diagonal neighboring tiles
       # First, find the coordinate of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for move_name, (d_row, d_col) in moves:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the blank space can be moved to the new tile
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [move_name], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile to its goal position
   # This heuristic relaxes the constraint that the blank space can only be moved diagonally, ie it presumes we can move the blank space in any direction to get to the goal state
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving the blank space to an adjacent tile is 1, which is always greater than or equal to the decrease in the Manhattan distance
   # Also the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(x, y) for x, row in enumerate(goal) for y, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
