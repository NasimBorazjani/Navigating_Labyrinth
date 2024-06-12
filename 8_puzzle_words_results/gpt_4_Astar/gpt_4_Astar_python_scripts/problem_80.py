
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('d', 'w', 'p', 'l', 't'),
                   ('e', 'i', 'd', 'e', 'c'),
                   ('_', 'q', 'e', 'i', 'r'),
                   ('m', 'e', 'c', 'u', 'r'),
                   ('y', 'u', 'a', 't', 'a'))
   # Define the goal state of the board
   goal_state = (('w', 'e', 'l', 't', '_'),
                ('e', 'd', 'd', 'i', 'c'),
                ('e', 'q', 'u', 'i', 'p'),
                ('m', 'a', 'c', 'e', 'r'),
                ('y', 'u', 'r', 't', 'a'))
   num_rows = 5
   num_cols = 5
   # Define the 4 possible diagonal directions of movement for the blank space
   directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


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
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col in directions:
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
                   # The direction of the blank space movement must be added to the actions
                   if d_row == 1 and d_col == 1:
                       direction = 'down-right'
                   elif d_row == 1 and d_col == -1:
                       direction = 'down-left'
                   elif d_row == -1 and d_col == 1:
                       direction = 'up-right'
                   elif d_row == -1 and d_col == -1:
                       direction = 'up-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # The heuristic relaxes the constraint that only the blank space can be moved, and only in the 4 diagonal directions
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving a tile reduces the Manhattan distance of that tile to its goal position by a max of 1 (if the tile is moved closer to its goal position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
