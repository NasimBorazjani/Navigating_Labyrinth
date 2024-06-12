
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 'c', 'a', 'a', 'n', 'k'),
                   ('h', 'm', 'r', 'l', 'i', 'g'),
                   ('h', 'i', 'o', 't', 'u', 'g'),
                   ('t', 'n', 'r', 't', 'a', 'c'),
                   ('z', 'y', 't', 'h', '_', 'm'))
   num_rows = 5
   num_cols = 6
   # Define the goal state of the board
   goal_state = (('c', 'h', 'a', 'n', 'k', '_'),
                 ('h', 'o', 'r', 'm', 'i', 'c'),
                 ('t', 'i', 'g', 't', 'a', 'g'),
                 ('t', 'o', 'r', 'n', 'a', 'l'),
                 ('z', 'y', 't', 'h', 'u', 'm'))
   # Define the directions of the 4 diagonal moves
   directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       # First, find the coordinates of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col in directions:
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
                   # The direction of the move is the direction in which the blank space was swapped in
                   if d_row == 1 and d_col == 1:
                       move = 'down-right'
                   elif d_row == 1 and d_col == -1:
                       move = 'down-left'
                   elif d_row == -1 and d_col == 1:
                       move = 'up-right'
                   elif d_row == -1 and d_col == -1:
                       move = 'up-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [move], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in the current state to its position in the goal state
   # The heuristic relaxes the constraint that only the blank space can be moved, and that it can only be swapped with one of its 4 diagonal neighbors
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving the blank space to an adjacent tile is 1, which is always greater than or equal to the decrease in the Manhattan distance of the tile that was swapped with the blank space
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
