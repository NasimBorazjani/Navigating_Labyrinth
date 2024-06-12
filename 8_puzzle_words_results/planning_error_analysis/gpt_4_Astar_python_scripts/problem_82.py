
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('i', 'e', 'k', 'k', 'a'),
                   ('b', 'e', 'f', 'a', 'r'),
                   ('g', 'a', '_', 'm', 'e'),
                   ('d', 'i', 'n', 'k', 'a'),
                   ('b', 'r', 'm', 't', 't'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'e', 'k', 'k', 'a'),
                 ('b', 'i', 'f', 'e', 'r'),
                 ('m', 'a', 'g', 'm', 'a'),
                 ('d', 'i', 'n', 'k', 'a'),
                 ('b', 'r', 'e', 't', 't'))
   num_rows = 5
   num_cols = 5
   # Define the 4 possible diagonal directions
   directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


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
       for d_row, d_col in directions:
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   # The action is represented as a tuple of the direction of the swap and the character that was swapped with the blank space
                   action = (direction_to_str((d_row, d_col)), new_state[blank_coord[0]][blank_coord[1]])
                   heapq.heappush(queue, (g + h, new_cost, actions + [action], new_state))
   return None


def direction_to_str(direction):
   # Convert the direction tuple to a string
   if direction == (1, 1):
       return 'down-right'
   elif direction == (1, -1):
       return 'down-left'
   elif direction == (-1, 1):
       return 'up-right'
   elif direction == (-1, -1):
       return 'up-left'


def heuristic(state, goal):
   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least its Manhattan distance to the goal
   # It's consistent because moving a tile reduces the Manhattan distance of that tile to the goal by at most 1 (if the move is toward the goal), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
