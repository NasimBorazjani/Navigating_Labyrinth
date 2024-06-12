
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('a', 'a', 'e', 'e', 'y'),
                   ('h', 'a', 'i', 't', 'h'),
                   ('_', 'r', 'k', 'n', 't'),
                   ('m', 'k', 'n', 'o', 'o'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('a', 'k', 'e', 'y', '_'),
                ('h', 'a', 'i', 'k', 'h'),
                ('t', 'r', 'o', 'n', 'e'),
                ('m', 'a', 'n', 't', 'o'))
   num_rows = 4
   num_cols = 5
   # Define the 4 possible diagonal directions of movement for the blank space
   directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
   # Define the direction names corresponding to the directions
   direction_names = ['down-right', 'down-left', 'up-right', 'up-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken to reach the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the blank space in any of the 4 diagonal directions
       # First, find the coordinates of the blank space in the current state
       blank_space_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for direction, direction_name in zip(directions, direction_names):
           new_row, new_col = blank_space_coord[0] + direction[0], blank_space_coord[1] + direction[1]
           # Check if the new coordinate is valid, ie if the blank space can be moved to the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_space_coord[0]][blank_space_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space_coord[0]][blank_space_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, g + 1, actions + [direction_name], new_state))
   return None


def heuristic(state, goal):
   # The heuristic function can be the sum of the Manhattan distances from each tile to its goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once
   # It's consistent because moving a tile reduces the Manhattan distance of the tile by a max of 1 (if the moved tile's goal position is in the direction of the move), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(x, y) for x, row in enumerate(goal) for y, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
